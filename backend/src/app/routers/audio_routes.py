# pylint: disable=R0801
"""FastAPI router for the chat services in the API."""

import logging

import whisper
from app.schemas.chat_schemas import TextInput
from app.services.chat_services import get_response
from app.services.speech_to_text_services import handle_audio_from_user
from app.services.text_to_speech_services import handle_text_to_speech
from app.utils.chat_utils.chat_utils import Chatbot
from fastapi import (
    APIRouter,
    HTTPException,
    UploadFile,
)
from fastapi.responses import FileResponse

# Set up the router
router = APIRouter(prefix="/voice-assistant")

# Set up logging
LOGGER = logging.getLogger("ChatService.audio-completions")

# Initialize the chatbot
LOGGER.info("Initializing chatbot...")
chatbot = Chatbot()
LOGGER.info("Chatbot initialized successfully.")

# Load Whisper model for speech-to-text
LOGGER.info("Loading Speech-to-Text model...")
whisper_model = whisper.load_model("base")
LOGGER.info("Speech-to-Text model loaded successfully.")


@router.post("/audio_interact")
async def handle_receive_audio_data(file: UploadFile):
    """Endpoint to interact with the chatbot."""
    LOGGER.info("Received file data: %s", file)
    try:
        LOGGER.info("Transcribing audio...")
        file_data = await file.read()  # Read the file data as bytes
        query = await handle_audio_from_user(
            model=whisper_model,
            file=file_data,
        )
        LOGGER.info("Transcribed audio successfully: %s", query)

        # Generate the chatbot response
        response = get_response(
            user_message=TextInput(text=query),
            chatbot=chatbot,
        )
        LOGGER.info("Generated response: %s", response.text)

        # Convert the response to audio
        LOGGER.info("Converting response to audio...")
        audio_response_path = handle_text_to_speech(text=response.text)

        # Return the response wrapped in a JSONResponse
        return FileResponse(
            audio_response_path,
            media_type="audio/mpeg",
            filename="ai_audio_reply.mp3",
            status_code=200,
        )

    except ValueError as e:  # pylint: disable=C0103
        LOGGER.error("Validation error: %s", str(e))
        raise HTTPException(status_code=400, detail="Invalid input data.") from e

    except Exception as e:  # pylint: disable=C0103
        LOGGER.error("Internal server error: %s", str(e))
        raise HTTPException(status_code=500, detail="An internal error occurred. Please try again.") from e
