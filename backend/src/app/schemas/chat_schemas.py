"""Pydantic schemas for the chat API."""

from pydantic import (
    BaseModel,
    Field,
)


class TextInput(BaseModel):
    """A Pydantic model for the input text to the chatbot."""

    text: str = Field(..., examples=["Hello, how are you?"], description="Input text for the chatbot.")


class TextOutput(BaseModel):
    """A Pydantic model for the output text from the chatbot."""

    text: str = Field(..., examples=["I am fine, thank you!"], description="Response text from the chatbot.")
