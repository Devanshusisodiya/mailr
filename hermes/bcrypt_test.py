from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed = pwd_context.hash("string@1234")
print("Hashed password:", hashed)
print("Verify:", pwd_context.verify("string@1234", hashed))
