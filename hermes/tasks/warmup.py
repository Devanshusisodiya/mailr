from hermes.utils.scheduler import celery_app
from hermes.utils.db import Session, engine
from hermes.models import WarmupEmail, WarmupSchedule, EmailSend, Contact, WarmupPair
from sqlmodel import select
from datetime import datetime, timedelta
import smtplib
import random
from email.mime.text import MIMEText

def get_recipients(db: Session, warmup_email: WarmupEmail, limit: int) -> list[str]:
    """Get recipients from p2p pairs first, then user contacts"""
    recipients = []
    
    # Get p2p pair emails first
    pairs = db.exec(
        select(WarmupPair)
        .where(
            (WarmupPair.warmup_email_a_id == warmup_email.id) | 
            (WarmupPair.warmup_email_b_id == warmup_email.id)
        )
        .where(WarmupPair.status == "active")
    ).all()
    
    for pair in pairs:
        partner_id = pair.warmup_email_b_id if pair.warmup_email_a_id == warmup_email.id else pair.warmup_email_a_id
        partner = db.get(WarmupEmail, partner_id)
        if partner and len(recipients) < limit:
            recipients.append(partner.email)
    
    # Fill remaining with user contacts
    if len(recipients) < limit:
        contacts = db.exec(
            select(Contact)
            .where(Contact.user_id == warmup_email.user_id)
            .limit(limit - len(recipients))
        ).all()
        recipients.extend([c.email for c in contacts])
    
    return recipients[:limit]


@celery_app.task
def send_email_task(warmup_email_id: str, recipient: str):
    """Send single email via SMTP"""
    with Session(engine) as db:
        warmup_email = db.get(WarmupEmail, warmup_email_id)
        if not warmup_email:
            return
        
        try:
            msg = MIMEText("This is a warmup email. Please ignore.")
            msg["Subject"] = "Test Email"
            msg["From"] = warmup_email.email
            msg["To"] = recipient
            
            with smtplib.SMTP(warmup_email.smtp_host, warmup_email.smtp_port) as server:
                server.starttls()
                server.login(warmup_email.smtp_username, warmup_email.smtp_password)
                server.send_message(msg)
            
            log = EmailSend(warmup_email_id=warmup_email.id, recipient_email=recipient, status="sent")
            db.add(log)
            db.commit()
        except Exception as e:
            log = EmailSend(warmup_email_id=warmup_email.id, recipient_email=recipient, status="failed")
            db.add(log)
            db.commit()


@celery_app.task
def send_warmup_emails():
    """Schedule emails throughout the day"""
    with Session(engine) as db:
        active_emails = db.exec(select(WarmupEmail).where(WarmupEmail.status == "active")).all()
        
        for warmup_email in active_emails:
            days_active = (datetime.utcnow() - warmup_email.created_at).days + 1
            schedule = db.exec(
                select(WarmupSchedule)
                .where(WarmupSchedule.warmup_email_id == warmup_email.id)
                .where(WarmupSchedule.day_number == days_active)
            ).first()
            
            if not schedule:
                continue
            
            today_sent = db.exec(
                select(EmailSend)
                .where(EmailSend.warmup_email_id == warmup_email.id)
                .where(EmailSend.sent_at >= datetime.utcnow().replace(hour=0, minute=0, second=0))
            ).all()
            
            remaining = schedule.daily_send_limit - len(today_sent)
            if remaining <= 0:
                continue
            
            recipients = get_recipients(db, warmup_email, remaining)
            
            # Distribute sends over 8 hours (9am-5pm work hours)
            work_hours = 8 * 3600  # seconds
            for i, recipient in enumerate(recipients):
                delay_seconds = random.randint(0, work_hours)
                send_email_task.apply_async(
                    args=[str(warmup_email.id), recipient],
                    countdown=delay_seconds
                )
