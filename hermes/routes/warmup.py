from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from hermes.utils.db import get_db
from hermes.models.models import WarmupEmail, WarmupSchedule, Contact
from hermes.services.pairing import create_pairs_for_new_email
from pydantic import BaseModel
from uuid import UUID

router = APIRouter(prefix="/warmup", tags=["warmup"])

class AddWarmupEmailRequest(BaseModel):
    email: str
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    imap_host: str | None = None
    imap_port: int | None = None


class AddContactRequest(BaseModel):
    email: str
    name: str | None = None


@router.post("/emails")
def add_warmup_email(req: AddWarmupEmailRequest, user_id: str, db: Session = Depends(get_db)):
    warmup = WarmupEmail(user_id=UUID(user_id), **req.dict())
    db.add(warmup)
    db.commit()
    db.refresh(warmup)
    
    # Create default 30-day schedule
    for day in range(1, 31):
        limit = min(5 + (day * 2), 50)  # Ramp from 5 to 50
        schedule = WarmupSchedule(warmup_email_id=warmup.id, day_number=day, daily_send_limit=limit)
        db.add(schedule)
    
    db.commit()
    create_pairs_for_new_email(db, warmup.id)
    return {"id": str(warmup.id)}




@router.post("/contacts")
def add_contact(req: AddContactRequest, user_id: str, db: Session = Depends(get_db)):
    contact = Contact(user_id=UUID(user_id), **req.dict())
    db.add(contact)
    db.commit()
    return {"id": str(contact.id)}


@router.get("/emails")
def list_warmup_emails(user_id: str, db: Session = Depends(get_db)):
    emails = db.exec(select(WarmupEmail).where(WarmupEmail.user_id == UUID(user_id))).all()
    return emails