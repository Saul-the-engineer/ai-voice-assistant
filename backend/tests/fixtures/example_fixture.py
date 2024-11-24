"""Fixture for the main app."""

from app.main import create_app
from fastapi.testclient import TestClient


def test_status_check():
    app = create_app()
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "running", "version": "1.0.0", "uptime": "API is up and running smoothly."}
