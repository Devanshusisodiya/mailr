import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from typing import Generator


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@localhost/postgres")
engine = create_engine(DATABASE_URL, echo=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
