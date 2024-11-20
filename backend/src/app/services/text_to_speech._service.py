"""This module converts text to speech using the Google Text-to-Speech API."""

from gtts import gTTS


def text_to_speech(text: str, file_path: str):
    """Convert text to speech and save the audio file to the specified path."""
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(file_path)
