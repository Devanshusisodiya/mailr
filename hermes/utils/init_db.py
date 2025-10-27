import sys
import os
sys.path.append(os.path.dirname(__file__) + "/..")
from sqlmodel import SQLModel
from utils.db import engine
from models.users import User  # Import all your models here

def init_db():
    print("📦 Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    init_db()
