from app.core.config import settings


def create_header() -> dict:
    return {settings.API_KEY_NAME: settings.API_KEY}