import typing as t
from fastapi import APIRouter, Depends
from sqlmodel import Session
from uuid import UUID
from utils.db import get_session
from dto.user import UserRequest, UserUpdate
from models.users import User
from services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=t.List[User])
def list_users(session: Session = Depends(get_session)):
    return user_service.get_all_users(session)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID, session: Session = Depends(get_session)):
    return user_service.get_user_by_id(session, user_id)

@router.post("/", response_model=User)
def create_user(user_request: UserRequest, session: Session = Depends(get_session)):
    return user_service.create_user(session, user_request)

@router.patch("/{user_id}", response_model=User)
def update_user(user_id: UUID, user_update: UserUpdate, session: Session = Depends(get_session)):
    return user_service.update_user(session, user_id, user_update)

@router.delete("/{user_id}")
def delete_user(user_id: UUID, session: Session = Depends(get_session)):
    return user_service.delete_user(session, user_id)
