# imports
from app.api.v1.api import api_router
from app.core.config import settings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    redoc_url=None,
)

# Set all CORS enabled origins
if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


# app startup event
@app.on_event("startup")
async def app_startup():
    """
    Do tasks related to app initialization.
    """


# app shutdown event
@app.on_event("shutdown")
async def app_shutdown():
    """
    Do tasks related to app termination.
    """
