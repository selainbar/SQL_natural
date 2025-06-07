import json
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from . import models, schemas


class UserDAL:
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_user(self, user_data: schemas.UserCreate):
        hashed_pw = bcrypt.hash(user_data.password)
        user = models.User(
            username=user_data.username,
            password=hashed_pw,
            databases=json.dumps(user_data.databases)  # Serialize list to JSON string
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_users(self):
        return self.db.query(models.User).all()

    def get_user_by_id(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def update_user(self, user_id: int, update_data: schemas.UserCreate):
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        user.username = update_data.username # type: ignore
        user.password = bcrypt.hash(update_data.password) # type: ignore
        user.databases = json.dumps(update_data.databases)  # type: ignore # Serialize list to JSON string
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user
