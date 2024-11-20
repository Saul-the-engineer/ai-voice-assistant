"""Chat service module containing the router for chat-related endpoints."""

import logging
import os

from app.schemas.chat_schemas import (
    TextInput,
    TextOutput,
)
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import pipeline


# Set up the model
def get_pipeline() -> pipeline:
    model_id = "meta-llama/Llama-3.2-1B-Instruct"
    return pipeline(
        task="text-generation",
        model=model_id,
        torch_dtype="bfloat16",
        device_map="auto",
    )


# Create the chatbot class
class Chatbot:
    """A chatbot that generates responses based on a given model pipeline."""

    def __init__(
        self,
        model_pipeline: pipeline,
        system_message: str = "You are a pirate chatbot who always responds in pirate speak!",
        max_history_tokens: int = 1024,
    ) -> None:

        self.pipe = model_pipeline
        self.messages = [{"role": "system", "content": system_message}]
        self.max_history_tokens = max_history_tokens

    def generate_response(self, user_message: TextInput, max_new_tokens: int = 512) -> str:
        # Add the user's message to the conversation history
        self.messages.append({"role": "user", "content": user_message})

        # Check if we need to trim the conversation history
        input_for_model = self.messages[-self.max_history_tokens :]

        # Generate response
        try:
            # Generates full conversation history, with response as the last message
            outputs = self.pipe(
                input_for_model,
                max_new_tokens=max_new_tokens,
            )
            # Generates list with dictionaries containing full conversation history
            # generated text; keys 'role', 'system', 'user', and 'content'
            generated_text = outputs[0]["generated_text"]

            content = generated_text[-1]["content"]

        except Exception as e:
            LOGGER.error(f"Error during response generation: {str(e)}")
            return "Sorry, I'm having trouble generating a response right now. Please try again later."

        # Add the chatbot's response to the conversation history
        self.messages.append({"role": "system", "content": content})

        return content


# Set up logging
LOGGER = logging.getLogger("ChatService.service")

# Load the Hugging Face API token
LOGGER.info("Loading Hugging Face API token")
load_dotenv()
login(token=os.getenv("HUGGINGFACE_TOKEN"))
LOGGER.info("Hugging Face API token loaded")

# Instantiate the pipeline and chatbot
LOGGER.info("Instantiating chatbot")
model = get_pipeline()
chatbot = Chatbot(model)
LOGGER.info("chatbot instantiated")


# generate a response
def generate_response(user_message: TextInput) -> TextOutput:
    """Generate a response to a user message."""
    response = TextOutput(text=chatbot.generate_response(user_message))
    return response
