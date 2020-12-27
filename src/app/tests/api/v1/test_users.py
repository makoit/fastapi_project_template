from fastapi.testclient import TestClient

from app.api.v1.endpoints.users_example import fake_users
from app.core.config import settings


def test_read_all_users(client: TestClient) -> None:

    r = client.get(f"{settings.API_V1_STR}/users/")
    assert 200 <= r.status_code < 300
    api_users = r.json()
    assert api_users == fake_users


def test_read_user_by_id(client: TestClient) -> None:

    user = fake_users[0]
    user_id = user.id
    r = client.get(f"{settings.API_V1_STR}/users/{user_id}")
    assert 200 <= r.status_code < 300
    api_user = r.json()
    existing_user = fake_users[0]
    assert existing_user
    assert existing_user.id == api_user["id"]


def test_create_new_user(client: TestClient) -> None:

    user = {"is_active": True, "is_superuser": True, "full_name": "Max Musterfrau"}

    r = client.post(f"{settings.API_V1_STR}/users/", json=user)
    assert 200 <= r.status_code < 300
    new_user = r.json()
    assert "id" in new_user
    assert new_user["is_active"] == user["is_active"]
    assert new_user["is_superuser"] == user["is_superuser"]
    assert new_user["full_name"] == user["full_name"]
