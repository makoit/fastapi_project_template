from fastapi.testclient import TestClient


from app.core.config import settings
from app.api.v1.endpoints.users_example import fake_users


def test_read_user(client: TestClient) -> None:

    user = fake_users[0]
    user_id = user.id
    r = client.get(f"{settings.API_V1_STR}/users/{user_id}")
    assert 200 <= r.status_code < 300
    api_user = r.json()
    existing_user = fake_users[0]
    assert existing_user
    assert existing_user.id == api_user["id"]
