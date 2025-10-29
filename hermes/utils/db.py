from sqlmodel import create_engine, Session, SQLModel
from hermes.config import settings
from typing import Generator
from hermes.models.models import (
    User,
    WarmupEmail,
    WarmupSchedule,
    Contact,
    WarmupPair,
    EmailSend
)


engine = create_engine(settings.database_url, echo=True)


def create_tables():
    """
    Strictly to be used for dev purposes only.
    """
    SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session