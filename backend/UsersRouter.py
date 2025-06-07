from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from JWTrouter import verify_token
from . import models
from . import schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

# In-memory storage for users
Users = {}
#get all users
@router.get("/", dependencies = [Depends(verify_token)])
async def getUsers():
    """
    Returns all users.
    """
    pass
#get a specific user
@router.get("/{user_id}", dependencies = [Depends(verify_token)])
async def getUser(user_id: str):
    """
    Returns a user with the given ID.
    """
    if user_id not in Users:
        return JSONResponse(status_code = 404, content = {"message": "user not found"})
    return Users[user_id]
    pass
#create a new user
@router.post("/", dependencies=[Depends(verify_token)])
async def createUser(username: str, password: str):
    """
    Creates a new user with the given username and password.
    """
    pass
#update a user
@router.put("/{user_id}", dependencies = [Depends(verify_token)])
async def updateUser(user_id: str, username: str, password: str ):
    """
    Updates a user with the given ID.
    """
    pass
#delete a user
@router.delete("/deleteUser", dependencies=[Depends(verify_token)])
async def deleteUser():
    """
    Delete a user by id.
    """
    pass   