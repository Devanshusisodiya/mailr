import typing as t
from fastapi import FastAPI, Depends
from utils.db import get_session
from sqlmodel import text, Session, select
from dto.user import UserRequest
from models.users import User
from routes import users  # import your route module

from hashlib import sha256


app = FastAPI()


@app.get("/")
async def health_check():
    return {
        "message": "Mailr API v0.0.1",
        "status": "ok"
    }

app.include_router(users.router)

