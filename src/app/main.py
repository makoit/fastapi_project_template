# imports
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from app.api.v1.api import api_router
from app.core.config import settings

from app.api.auth.basic_auth import auth_base_user_for_docs

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=None, 
    redoc_url=None, 
    openapi_url=None
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

# include api router
app.include_router(api_router, prefix=settings.API_V1_STR)


# set up api doc with
@app.get(f"{settings.API_V1_STR}/openapi.json", tags=["documentation"], dependencies=[Depends(auth_base_user_for_docs)], include_in_schema=False)
async def get_open_api_endpoint():
    response = JSONResponse(
        get_openapi(title="FastAPI security example", version=1.0, routes=app.routes)
    )
    return response

@app.get(f"{settings.API_V1_STR}/docs", tags=["documentation"], dependencies=[Depends(auth_base_user_for_docs)], include_in_schema=False)
async def get_documentation():
    response = get_swagger_ui_html(openapi_url=f"{settings.API_V1_STR}/openapi.json", title="API Documentation")
    return response


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
