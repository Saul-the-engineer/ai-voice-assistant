"""Pydantic schemas for the chat API."""

from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


class TextOutput(BaseModel):
    text: str
