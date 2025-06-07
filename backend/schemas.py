from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str
    databases: List[str]

class UserOut(BaseModel):
    id: int
    username: str
    databases: List[str]

class UserUpdate(BaseModel):
    username: str
    password: str
    databases: List[str]

class Config:
        orm_mode = True
