from sqlmodel import Session, select
from hermes.models.models import WarmupEmail, WarmupPair
from uuid import UUID
import random

def create_pairs_for_new_email(db: Session, new_warmup_email_id: UUID):
    """Pair new email, avoiding same user and same domain"""
    new_email = db.get(WarmupEmail, new_warmup_email_id)
    if not new_email:
        return
    
    new_domain = new_email.email.split('@')[1]
    
    all_active = db.exec(
        select(WarmupEmail)
        .where(WarmupEmail.status == "active")
        .where(WarmupEmail.id != new_warmup_email_id)
        .where(WarmupEmail.user_id != new_email.user_id)  # Different user
    ).all()
    
    candidates = []
    for email in all_active:
        email_domain = email.email.split('@')[1]
        if email_domain == new_domain:  # Skip same domain
            continue
            
        pair_count = db.exec(
            select(WarmupPair)
            .where(
                ((WarmupPair.warmup_email_a_id == email.id) | (WarmupPair.warmup_email_b_id == email.id))
            )
        ).all()
        
        if len(pair_count) < 3:
            candidates.append(email)
    
    targets = random.sample(candidates, min(3, len(candidates)))
    
    for target in targets:
        pair = WarmupPair(
            warmup_email_a_id=new_warmup_email_id,
            warmup_email_b_id=target.id
        )
        db.add(pair)
    
    db.commit()