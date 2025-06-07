from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    databases = Column(String)  # Store as JSON string or comma-separated values

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"