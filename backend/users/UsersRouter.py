from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .DAL import UserDAL
from .Dependencies import get_db
from .users import schemas
from backend.jwtRouter.JWTrouter import verify_token
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.UserOut], dependencies=[Depends(verify_token)])
async def get_users(db: Session = Depends(get_db)):
    dal = UserDAL(db)
    return dal.get_users()

@router.get("/{user_id}", response_model=schemas.UserOut, dependencies=[Depends(verify_token)])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    dal = UserDAL(db)
    user = dal.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=schemas.UserOut, dependencies=[Depends(verify_token)])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    dal = UserDAL(db)
    return dal.create_user(user)

@router.put("/{user_id}", response_model=schemas.UserOut, dependencies=[Depends(verify_token)])
async def update_user(user_id: int, update_data: schemas.UserUpdate, db: Session = Depends(get_db)):
    dal = UserDAL(db)
    updated_user = dal.update_user(user_id, update_data) 
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=schemas.UserOut, dependencies=[Depends(verify_token)])
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    dal = UserDAL(db)
    deleted_user = dal.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user