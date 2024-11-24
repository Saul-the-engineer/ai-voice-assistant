"""Test the main module."""

import os
import tempfile
from unittest.mock import patch

import pytest
from app.main import (
    create_app,
    shutdown_event,
    startup_event,
)
from app.utils.file_utils import TMP_FOLDER_NAME
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


@patch("app.main.create_secure_tmp_folder")
@patch("app.main.LOGGER.info")
def test_startup_event(mock_logger, mock_create_tmp, client):  # Include client if needed for context
    startup_event()
    mock_create_tmp.assert_called_once()
    mock_logger.assert_called_with("Application startup complete. Temporary directory is ready.")


@patch("app.main.shutil.rmtree")
@patch("app.main.LOGGER.info")
def test_shutdown_event(mock_logger, mock_rmtree, client):  # Include client if needed for context
    tmp_dir_path = os.path.join(tempfile.gettempdir(), TMP_FOLDER_NAME)
    with patch("os.path.exists", return_value=True):
        shutdown_event()
        mock_rmtree.assert_called_once_with(tmp_dir_path)
        mock_logger.assert_called_with("Deleted temporary directory: %s", tmp_dir_path)
