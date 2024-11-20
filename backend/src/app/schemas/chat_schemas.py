"""Pydantic schemas for the chat API."""

from pydantic import BaseModel


class TextInput(BaseModel):
    """A Pydantic model for the input text to the chatbot."""

    text: str


class TextOutput(BaseModel):
    """A Pydantic model for the output text from the chatbot."""

    text: str
