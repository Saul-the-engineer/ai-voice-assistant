import logging
import os
import shutil
import tempfile

from app.routers import (
    audio_routes,
    text_routes,
)
from app.utils.file_utils import (
    TMP_FOLDER_NAME,
    create_secure_tmp_folder,
)
from app.utils.project_config import setup_app_config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Centralized logging configuration
log_level = logging.DEBUG if os.getenv("ENV") == "development" else logging.INFO
logging.basicConfig(format="%(levelname)s - %(asctime)s - %(filename)s - %(message)s", level=log_level)
LOGGER = logging.getLogger("ChatBot Service")

# Setup the application configuration
setup_app_config()


def startup_event():
    """Event handler for application startup."""
    create_secure_tmp_folder()
    LOGGER.info("Application startup complete. Temporary directory is ready.")


def shutdown_event():
    """Event handler for application shutdown."""
    tmp_dir_path = os.path.join(tempfile.gettempdir(), TMP_FOLDER_NAME)
    if os.path.exists(tmp_dir_path):
        shutil.rmtree(tmp_dir_path)
        LOGGER.info(f"Deleted temporary directory: {tmp_dir_path}")


def create_app() -> FastAPI:
    """
    Application factory for FastAPI.
    This function creates and returns a new FastAPI application instance.
    """
    app = FastAPI()

    # Origins that are allowed to make requests to the API
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    # CORS middleware to protect the API from Cross-Origin Resource Sharing (CORS) attacks
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Status check endpoint
    @app.get("/")
    def status_check():
        """Status check endpoint."""
        return {"status": "running", "version": "1.0.0", "uptime": "API is up and running smoothly."}

    # Include the router
    app.include_router(text_routes.router)
    app.include_router(audio_routes.router)

    # Add event handlers for startup and shutdown
    app.router.add_event_handler("startup", startup_event)
    app.router.add_event_handler("shutdown", shutdown_event)

    return app


if __name__ == "__main__":
    import uvicorn

    app = create_app()  # Create a FastAPI instance using the factory function
    uvicorn.run(app, host="0.0.0.0", port=8000)

    app = create_app()  # Create a FastAPI instance using the factory function
    uvicorn.run(app, host="0.0.0.0", port=8000)
