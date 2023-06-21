from pytest import fixture
from rest_framework.test import APIClient


api_client = APIClient()
user_model_register = dict(
    email="test_email@mail.ru",
    username="test_user",
    avatar="",
    password=123456,
    password2=123456,
)
user_model_login = dict(email="test_email@mail.ru", password=123456)


@fixture
def client():
    return api_client


@fixture
def user_register():
    return user_model_register


@fixture
def user_login():
    return user_model_login


@fixture
def user():
    api_client.post("/accounts/register", user_model_register)
    resp = api_client.post("/accounts/login", user_model_login)

    return resp
