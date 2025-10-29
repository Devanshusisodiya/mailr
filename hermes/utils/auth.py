from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from hermes.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_token(user_id: str) -> str:
    expire = datetime.toda() + timedelta(days=7)
    return jwt.encode({"sub": user_id, "exp": expire}, settings.secret_key, algorithm="HS256")