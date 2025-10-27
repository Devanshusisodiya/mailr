import typing as t
from fastapi import FastAPI, Depends
from utils.db import get_session
from sqlmodel import text, Session, select
from dto.user import UserRequest
from models.users import User
from hashlib import sha256


app = FastAPI()


@app.get("/")
async def health_check():
    return {
        "message": "Mailr API v0.0.1",
        "status": "ok"
    }

@app.get("/users")
async def read_users(session: Session =Depends(get_session)) -> t.List[User]:
    users = session.exec(select(User))
    return [user for user in users.all()]


@app.post("/users")
async def create_user(user_request: UserRequest, session=Depends(get_session)):

    user = User(
        hashed_password=sha256(user_request.password.encode('utf-8')).hexdigest(),
        **user_request.model_dump(mode="json")
    )
    session.add(user)
    session.commit()

    return user.id
