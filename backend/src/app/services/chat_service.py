"""Chat service module containing the router for chat-related endpoints."""

import logging

from app.schemas.chat_schemas import TextOutput
from langchain import ConversationChain
from langchain.llms import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory
from transformers import pipeline

# Set up logging
LOGGER = logging.getLogger("ChatService.service")

# Load the model
llm = HuggingFacePipeline(pipeline("text-generation", model="gpt-2"))

# Create chat memory for the chatbot
chat_memory = ConversationBufferMemory(max_tokens=1024, max_turns=5)

# Initialize Conversation Chain
conversation_chain = ConversationChain(llm=llm, memory=chat_memory)


class ChatService:
    def generate_response(self, text: str) -> TextOutput:
        """Process the text and return a relevant response to the user."""
        LOGGER.info(f"Classifying text: {text}")
        response = conversation_chain.run(input_text=text)
        return TextOutput(text=response["generated_text"])
