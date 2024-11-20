"""Chat service module containing the router for chat-related endpoints."""

import logging

from app.schemas.chat_schemas import (
    TextInput,
    TextOutput,
)
from app.utils.chat_utils.chat_utils import Chatbot

# Set up logging
LOGGER = logging.getLogger("ChatService.service")


# generate a response (updated to accept chatbot instance explicitly)
def get_response(user_message: TextInput, chatbot: Chatbot) -> TextOutput:
    """Generate a response to a user message."""
    try:
        LOGGER.debug(f"Received user message: {user_message.text}")
        response_text = chatbot.generate_response(user_message)
        return TextOutput(text=response_text)
    except RuntimeError as e:
        LOGGER.error(f"Failed to generate response: {str(e)}")
        return TextOutput(text="Sorry, I'm having trouble generating a response right now.")
