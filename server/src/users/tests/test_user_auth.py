import pytest


def register_user(user, client):
    resp = client.post("/accounts/register", user)

    return resp


@pytest.mark.django_db
def test_user_register(client, user_register):
    resp = register_user(client=client, user=user_register)

    assert resp.data["user"]["name"] == user_register["name"]


@pytest.mark.django_db
def test_user_login(client, user_login, user_register):
    register_user(client=client, user=user_register)
    resp = client.post("/accounts/login", user_login)

    assert resp.data["msg"] == "Login Success"
