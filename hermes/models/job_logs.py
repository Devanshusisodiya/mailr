from typing import Optional, Dict, Any
from datetime import datetime
from sqlmodel import Field, JSON
from sqlalchemy import Column, DateTime, ForeignKey
from uuid import UUID, uuid4

from models.common import CommonBase

class EmailLog(CommonBase, table=True):
    __tablename__ = "email_logs"

    warmup_task_id: UUID = Field(foreign_key="warmup_jobs.id", nullable=False, index=True)
    event_type: str = Field(nullable=False)
    event_time: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(DateTime, nullable=False))
    metadata: Optional[Dict[str, Any]] = Field(default=None, sa_column=Column(JSON, nullable=True))

    def __repr__(self) -> str:
        return f"EmailLog(id={self.id!r}, event_type={self.event_type!r})"
