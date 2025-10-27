from typing import Optional
from datetime import datetime
from sqlmodel import Field
from sqlalchemy import Column, DateTime, ForeignKey, Text, Boolean
from uuid import UUID, uuid4

from models.common import CommonBase

class WarmupJobs(CommonBase, table=True):
    __tablename__ = "warmup_jobs"

    sender_account_id: UUID = Field(foreign_key="email_accounts.id", nullable=False, index=True)
    recipient_account_id: UUID = Field(foreign_key="email_accounts.id", nullable=False, index=True)

    subject: Optional[str] = Field(default=None)
    body: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    scheduled_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))
    sent_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    opened: bool = Field(default=False, sa_column=Column(Boolean, nullable=False))
    replied: bool = Field(default=False, sa_column=Column(Boolean, nullable=False))
    clicked: bool = Field(default=False, sa_column=Column(Boolean, nullable=False))

    def __repr__(self) -> str:
        return f"WarmupJob(id={self.id!r}, sender={self.sender_account_id!r}, recipient={self.recipient_account_id!r})"
