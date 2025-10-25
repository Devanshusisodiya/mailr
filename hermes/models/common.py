from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Column, Field, DateTime

class CommonBase(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False, index=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime, default=datetime.utcnow, nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    ))
