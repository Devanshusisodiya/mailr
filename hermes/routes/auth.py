from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from hermes.utils.db import get_db
from hermes.models.models import User
from hermes.utils.auth import hash_password, verify_password, create_token
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

class SignupRequest(BaseModel):
    email: str
    password: str


@router.post("/signup")
def signup(req: SignupRequest, db: Session = Depends(get_db)):
    if db.exec(select(User).where(User.email == req.email)).first():
        raise HTTPException(400, "Email exists")
    user = User(email=req.email, password_hash=hash_password(req.password))
    db.add(user)
    db.commit()
    return {"token": create_token(str(user.id))}


@router.post("/login")
def login(req: SignupRequest, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.email == req.email)).first()
    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")
    return {"token": create_token(str(user.id))}