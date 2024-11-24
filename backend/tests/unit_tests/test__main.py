"""Test the main module."""


import pytest
from app.main import create_app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")  # Ensures the app is created once per session
def client():
    app = create_app()
    with TestClient(app) as test_client:
        yield test_client


def test_status_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "running", "version": "1.0.0", "uptime": "API is up and running smoothly."}


def test_create_app(client):
    """Test the create_app function using the TestClient from the fixture."""
    # Debugging output
    for route in client.app.routes:
        print(route.path)

    # Assert that routers are included
    assert any(
        route.path == "/voice-assistant/text_interact" for route in client.app.routes
    ), "Route /voice-assistant/text_interact is not found"
    assert any(
        route.path == "/voice-assistant/audio_interact" for route in client.app.routes
    ), "Route /voice-assistant/audio_interact is not found"
