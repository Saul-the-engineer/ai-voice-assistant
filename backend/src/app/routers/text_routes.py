# pylint: disable=R0801
"""FastAPI router for the chat services in the API."""

import logging

from app.schemas.chat_schemas import (
    TextInput,
    TextOutput,
)
from app.services.chat_services import get_response
from app.utils.chat_utils.chat_utils import Chatbot
from fastapi import (
    APIRouter,
    HTTPException,
)
from fastapi.responses import JSONResponse

# Set up the router
router = APIRouter(prefix="/voice-assistant")

# Set up logging
LOGGER = logging.getLogger("ChatService.completions")

"""
future improvement:
/chat/history: This endpoint will return the chat history for a given conversation.
/chat/settings: This endpoint will allow the user to set the chatbot's settings, such as the system message and the maximum history tokens.
/chat/rag_response: This endpoint will return a response from the chatbot using the RAG model.
"""

# Initialize the chatbot
LOGGER.info("Initializing chatbot...")
chatbot = Chatbot()
LOGGER.info("Chatbot initialized successfully.")


@router.post(
    "/text_interact",
    response_model=TextOutput,
    responses={
        200: {"description": "Successful response", "model": TextOutput},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
)
async def chat_endpoint(user_input: TextInput) -> JSONResponse:
    """Endpoint to interact with the chatbot."""
    LOGGER.info("Received input for chat: %s", user_input.text)

    try:
        # Generate the chatbot response
        response = get_response(user_input, chatbot)
        LOGGER.info("Generated response: %s", response.text)

        # Return the response wrapped in a JSONResponse
        return JSONResponse(content=response.model_dump(), status_code=200)

    except ValueError as e:  # pylint: disable=C0103
        LOGGER.error("Validation error: %s", str(e))
        raise HTTPException(status_code=400, detail="Invalid input data.") from e

    except Exception as e:  # pylint: disable=C0103
        LOGGER.error("Internal server error: %s", str(e))
        raise HTTPException(status_code=500, detail="An internal error occurred. Please try again.") from e
