from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[str] = None
