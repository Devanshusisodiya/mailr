from typing import Optional
from datetime import datetime
from sqlmodel import Field
from sqlalchemy import Column, DateTime
from models.common import CommonBase

class SMTPConfig(CommonBase, table=True):
    __tablename__ = "smtp_configs"

    host: str = Field(nullable=False)
    port: int = Field(nullable=False)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)

    def __repr__(self) -> str:
        return f"SMTPConfig(id={self.id!r}, host={self.host!r}, username={self.username!r})"
