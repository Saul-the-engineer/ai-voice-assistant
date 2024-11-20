"""This module contains the speech to text service for the API."""

import whisper

# Load the model once and reuse it for each transcription
model = whisper.load_model("base")


def transcribe_audio(file_path: str) -> str:
    """Transcribe the audio at the given file path using the Whisper model."""
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]
