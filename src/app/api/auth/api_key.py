from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, status, HTTPException
from app.core.config import settings

api_key_header = APIKeyHeader(name=settings.API_KEY_NAME, auto_error=True)

async def get_api_key(api_key_header: str = Security(api_key_header)):

    if api_key_header == settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )