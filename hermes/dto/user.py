import typing as t
from typing import Optional
from pydantic import BaseModel, Field, EmailStr



class UserRequest(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None  # optional for updates
