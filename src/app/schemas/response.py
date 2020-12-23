from pydantic import BaseModel


class ResponseMessage(BaseModel):
    details: str
