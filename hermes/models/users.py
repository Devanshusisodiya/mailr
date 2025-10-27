from typing import Optional
from datetime import datetime
from sqlmodel import Field
from sqlalchemy import Column, DateTime
from models.common import CommonBase

class User(CommonBase, table=True):
    __tablename__ = "users"

    name: str = Field(nullable=False, index=True)
    email: str = Field(nullable=False, unique=True, index=True)
    hashed_password: str = Field(nullable=False)
    last_login: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"