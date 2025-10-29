from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional, List

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(max_length=255, unique=True, index=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relations
    warmup_emails: List["WarmupEmail"] = Relationship(back_populates="user")
    contacts: List["Contact"] = Relationship(back_populates="user")

class WarmupEmail(SQLModel, table=True):
    __tablename__ = "warmup_emails"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id")
    email: str = Field(max_length=255)
    smtp_host: str = Field(max_length=255)
    smtp_port: int
    smtp_username: str = Field(max_length=255)
    smtp_password: str = Field(max_length=255)
    imap_host: Optional[str] = Field(default=None, max_length=255)
    imap_port: Optional[int] = None
    status: str = Field(default="active", max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relations
    user: Optional["User"] = Relationship(back_populates="warmup_emails")
    schedules: List["WarmupSchedule"] = Relationship(back_populates="warmup_email")
    email_sends: List["EmailSend"] = Relationship(back_populates="warmup_email")

class WarmupSchedule(SQLModel, table=True):
    __tablename__ = "warmup_schedules"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    warmup_email_id: UUID = Field(foreign_key="warmup_emails.id")
    day_number: int
    daily_send_limit: int
    
    # Relations
    warmup_email: Optional["WarmupEmail"] = Relationship(back_populates="schedules")

class Contact(SQLModel, table=True):
    __tablename__ = "contacts"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id")
    email: str = Field(max_length=255)
    name: Optional[str] = Field(default=None, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relations
    user: Optional["User"] = Relationship(back_populates="contacts")

class WarmupPair(SQLModel, table=True):
    __tablename__ = "warmup_pairs"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    warmup_email_a_id: UUID = Field(foreign_key="warmup_emails.id")
    warmup_email_b_id: UUID = Field(foreign_key="warmup_emails.id")
    status: str = Field(default="active", max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class EmailSend(SQLModel, table=True):
    __tablename__ = "email_sends"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    warmup_email_id: UUID = Field(foreign_key="warmup_emails.id")
    recipient_email: str = Field(max_length=255)
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(max_length=50)
    
    # Relations
    warmup_email: Optional["WarmupEmail"] = Relationship(back_populates="email_sends")