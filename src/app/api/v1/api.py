from app.api.v1.endpoints import users_example
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(users_example.router, prefix="/users", tags=["users"])
