"""This module contains the FastAPI router for the chat services in the API."""

import logging

from app.schemas.chat_schemas import (
    TextInput,
    TextOutput,
)
from app.services.chat_services import ChatService
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Set up the router
router = APIRouter()

test = [
    "test1",
    "test2",
    "test3",
]

# Set up logging
LOGGER = logging.getLogger("ChatService.completions")

# Initialize the ChatService
chat_service = ChatService()


@router.post("/chat/interact", response_model=TextOutput)
async def predict_fakeness(text: TextInput):
    """Make a prediction on the fakeness of a statement."""
    LOGGER.info(f"Received text for analysis: {text.text}")
    try:
        output_model = chat_service.predict(text.text)
        LOGGER.info(f"Generated output: {output_model}")
        return output_model
    except Exception as e:
        LOGGER.error(f"Error during prediction: {str(e)}")
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
