from fastapi import APIRouter, Security
from app.api.auth.api_key import get_api_key

from app.api.v1.endpoints import users_example

api_router = APIRouter()
api_router.include_router(users_example.router, prefix="/users", tags=["users"], dependencies=[Security(get_api_key)])
