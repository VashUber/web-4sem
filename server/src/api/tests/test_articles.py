import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_top_articles(client):
    resp = client.get("/articles/top")

    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_articles(client):
    resp = client.get("/articles/?page=1")

    assert resp.status_code == status.HTTP_200_OK
