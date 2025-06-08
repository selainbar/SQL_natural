from fastapi import FastAPI
from users.UsersRouter import router as users_router
from jwtRouter.JWTrouter import router as jwt_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
security_scheme = {
    "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
}
#boiler plate for making the jwt token available in the swagger UI
original_openapi = app.openapi
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = original_openapi()
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}
    if "securitySchemes" not in openapi_schema["components"]:
        openapi_schema["components"]["securitySchemes"] = {}
    openapi_schema["components"]["securitySchemes"] = security_scheme
    openapi_schema["security"] = [{"bearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema
#changing the openapi schema to include the jwt token changes
app.openapi = custom_openapi
#generic cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, # for cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(jwt_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

