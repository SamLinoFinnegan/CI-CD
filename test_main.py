import pytest

from main import app

@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_proxy(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data 