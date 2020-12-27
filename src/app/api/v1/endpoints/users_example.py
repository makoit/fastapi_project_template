import uuid
from typing import List

from fastapi import APIRouter, status  # , HTTPException
from fastapi.responses import JSONResponse

from app import schemas

router = APIRouter()

fake_users = [
    schemas.UserInDBBase(
        is_active=True,
        is_superuser=True,
        full_name="Max Mustermann",
        id="1234",
    ),
    schemas.UserInDBBase(
        is_active=True,
        is_superuser=False,
        full_name="Hans Test",
        id="5678",
    ),
]


# read all users endpoint
@router.get(
    "/",
    response_model=List[schemas.UserInDBBase],
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": schemas.ResponseMessage, "description": "No users found"},
        200: {
            "description": "Users requested",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "is_active": True,
                            "is_superuser": True,
                            "full_name": "Max Mustermann",
                            "id": "1234",
                        },
                        {
                            "is_active": True,
                            "is_superuser": False,
                            "full_name": "Hans Meier",
                            "id": "5678",
                        },
                    ]
                }
            },
        },
    },
)
def read_users():
    """
    Retrieve users.
    """
    users = fake_users
    # users = []

    if not users:
        # raise HTTPException(
        #     status_code=status.HTTP_404_NOT_FOUND, detail="No users found"
        # )
        return JSONResponse(status_code=404, content={"details": "Users not found"})

    return users


# read a user by specific id
@router.get(
    "/{id}",
    response_model=schemas.UserInDBBase,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": schemas.ResponseMessage, "description": "User not found"},
        status.HTTP_200_OK: {
            "description": "User requested",
            "content": {
                "application/json": {
                    "example": {
                        "is_active": True,
                        "is_superuser": True,
                        "full_name": "Max Mustermann",
                        "id": "1234",
                    }
                }
            },
        },
    },
)
async def read_user_by_id(id: str):
    """
    Retrieve user by ID
    """

    user = [user for user in fake_users if user.id == id][0]

    if not user:
        return JSONResponse(status_code=404, content={"details": "User not found"})

    return user


# create a new user
@router.post(
    "/",
    response_model=schemas.UserInDBBase,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "User created",
            "content": {
                "application/json": {
                    "example": {
                        "is_active": True,
                        "is_superuser": True,
                        "full_name": "Max Mustermann",
                        "id": "1234",
                    }
                }
            },
        },
    },
)
def create_user(new_user: schemas.UserBase):
    """
    Create new user.
    """

    new_user = schemas.UserInDBBase(
        is_active=new_user.is_active,
        is_superuser=new_user.is_superuser,
        full_name=new_user.full_name,
        id=str(uuid.uuid1()),
    )
    fake_users.append(new_user)

    return new_user


# update a user by specific id
@router.put(
    "/{id}",
    response_model=schemas.UserInDBBase,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": schemas.ResponseMessage, "description": "User not found"},
        200: {
            "description": "User updated",
            "content": {
                "application/json": {
                    "example": {
                        "is_active": True,
                        "is_superuser": True,
                        "full_name": "Max Mustermann",
                        "id": "1234",
                    }
                }
            },
        },
    },
)
async def update_user(id: str, user: schemas.UserBase):
    """
    Update user by ID.
    """
    user_update = schemas.UserInDBBase(
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        full_name=user.full_name,
        id=id,
    )

    find_user = [user for user in fake_users if user.id == id][0]

    if not find_user:
        return JSONResponse(status_code=404, content={"details": "User not found"})
    else:
        fake_users[:] = [user_update for user in fake_users if user.id == id]
        return user_update


# delete user by specific id
@router.delete(
    "/{id}",
    response_model=schemas.UserInDBBase,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": schemas.ResponseMessage, "description": "User not found"},
        200: {
            "description": "User deleted",
            "content": {
                "application/json": {
                    "example": {
                        "is_active": True,
                        "is_superuser": True,
                        "full_name": "Max Mustermann",
                        "id": "1234",
                    }
                }
            },
        },
    },
)
async def delete_user(id: str):
    """
    Delete user by ID.
    """

    user_to_delete = [user for user in fake_users if user.id == id][0]

    if not user_to_delete:
        return JSONResponse(status_code=404, content={"details": "User not found"})
    else:
        fake_users.remove(user_to_delete)
        return user_to_delete
