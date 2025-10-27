import typing as t
from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    name: str
    email: str
    password: str
