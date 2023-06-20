import pytest
from rest_framework import status


@pytest.mark.django_db
def test_comments(client):
    resp = client.get("/articles/1/comments/")

    assert resp.status_code == status.HTTP_200_OK
