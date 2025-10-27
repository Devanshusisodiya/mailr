from typing import Optional
from datetime import datetime
from sqlmodel import Field
from sqlalchemy import Column, DateTime, Float, ForeignKey
from uuid import UUID, uuid4

from models.common import CommonBase

class EmailAccount(CommonBase, table=True):
    __tablename__ = "email_accounts"

    user_id: UUID = Field(foreign_key="users.id", nullable=False, index=True)
    smtp_config_id: UUID = Field(foreign_key="smtp_configs.id", nullable=False, index=True)

    email_address: str = Field(nullable=False, unique=True, index=True)
    imap_host: Optional[str] = Field(default=None)
    imap_port: Optional[int] = Field(default=None)
    imap_username: Optional[str] = Field(default=None)
    imap_password: Optional[str] = Field(default=None)
    warmup_status: Optional[str] = Field(default=None)
    reputation_score: Optional[float] = Field(default=None, sa_column=Column(Float, nullable=True))

    def __repr__(self) -> str:
        return f"EmailAccount(id={self.id!r}, email={self.email_address!r})"
