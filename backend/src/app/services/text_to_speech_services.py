"""Convert text-to-speech using the Google Text-to-Speech API."""

from app.utils.file_utils import create_unique_tmp_file
from gtts import gTTS


def text_to_speech_to_file(text: str, file_path: str):
    """Convert text to speech and save the audio file to the specified path."""
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(file_path)


def handle_text_to_speech(text: str) -> str:
    """Convert text to speech and return the path to the audio file."""
    # Generate a unique temporary file path for storing the MP3 file
    output_audio_file_path = create_unique_tmp_file("ai_audio_reply.mp3")
    # Convert text to speech and save as an MP3 file
    text_to_speech_to_file(text, output_audio_file_path)
    return output_audio_file_path
