from fastapi import FastAPI
from .users.UsersRouter import router as users_router
from .jwtRouter.JWTrouter import router as jwt_router

app = FastAPI()

app.include_router(users_router)
app.include_router(jwt_router)