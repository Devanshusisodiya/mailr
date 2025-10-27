from typing import List
from uuid import UUID
from sqlmodel import Session, select
from fastapi import HTTPException, status
from passlib.context import CryptContext

from models.users import User
from dto.user import UserRequest, UserUpdate


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_all_users(session: Session) -> List[User]:
    return session.exec(select(User)).all()


def get_user_by_id(session: Session, user_id: UUID) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def create_user(session: Session, user_request: UserRequest) -> User:
    # Check for duplicate email
    existing_user = session.exec(select(User).where(User.email == user_request.email)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Hash password securely
    print("password before bcrypt :",user_request.password)
    print("password before bcrypt:", user_request.password, type(user_request.password))

    hashed_password = hash_password(user_request.password)

    user = User(
        hashed_password=hashed_password,
        **user_request.model_dump(exclude={"password"})
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_user(session: Session, user_id: UUID, user_update: UserUpdate) -> User:
    user = get_user_by_id(session, user_id)
    data = user_update.model_dump(exclude_unset=True)

    # Prevent duplicate emails
    if "email" in data:
        existing = session.exec(
            select(User).where(User.email == data["email"], User.id != user_id)
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already in use")

    # Rehash password if provided
    if "password" in data:
        data["hashed_password"] = hash_password(data.pop("password"))

    for key, value in data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def delete_user(session: Session, user_id: UUID) -> dict:
    user = get_user_by_id(session, user_id)
    session.delete(user)
    session.commit()
    return {"message": f"User {user.email} deleted successfully"}
