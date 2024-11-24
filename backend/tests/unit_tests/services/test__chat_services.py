"""Test chat services module."""

from app.main import create_app
from fastapi.testclient import TestClient
from pytest import fixture


@fixture
def client():
    app = create_app()
    return TestClient(app)


def test_chat_endpoint_success(client):
    request_data = {"text": "Hello, how are you?"}
    response = client.post("/voice-assistant/text_interact", json=request_data)
    assert response.status_code == 200


def test_chat_endpoint_failure(client):
    request_data = {"wrong_key": "This will fail"}
    response = client.post("/voice-assistant/text_interact", json=request_data)
    assert response.status_code == 422


def test_chat_wrong_input(client):
    request_data = {"text": 123}
    response = client.post("/voice-assistant/text_interact", json=request_data)
    assert response.status_code == 422
