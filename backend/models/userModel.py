from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    databases = Column(String)  # You can use a JSON or Text field for multiple databases

# Pydantic schemas
class UserCreate(BaseModel):
    username: str
    password: str
    databases: list[str]  # Assuming databases is a list of strings

class UserRead(BaseModel):
    id: int
    username: str
    databases: str

    class Config:
        orm_mode = True
        # Database connection helper
        def get_db():
            engine = create_engine("postgresql://username:password@localhost:5432/Users")  # PostgreSQL connection URL
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()
