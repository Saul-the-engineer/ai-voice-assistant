"""Chat utils module containing the chatbot class and model pipeline."""

import os

from app.schemas.chat_schemas import TextInput
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import pipeline


# Set up the model
def get_pipeline() -> pipeline:
    # Check if the environment variables are loaded
    if not os.getenv("HUGGINGFACE_TOKEN"):
        print("Environment variables not loaded. Loading from .env file...")
        load_dotenv()

    # Authenticate with Hugging Face Hub
    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
    if not huggingface_token:
        raise ValueError("HUGGINGFACE_TOKEN is not set in the environment variables or .env file.")

    login(token=huggingface_token)

    # Load the model pipeline
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
        model_pipeline: pipeline = None,
        system_message: str = "You are a pirate chatbot who always responds in pirate speak!",
        max_history_tokens: int = 1024,
    ) -> None:

        # Use provided pipeline or initialize a default one
        self.pipe = model_pipeline or get_pipeline()
        self.messages = [{"role": "system", "content": system_message}]
        self.max_history_tokens = max_history_tokens

    def generate_response(self, user_message: TextInput, max_new_tokens: int = 512) -> str:
        # Add the user's message to the conversation history
        self.messages.append({"role": "user", "content": user_message.text})

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
            raise RuntimeError("Error generating chatbot response") from e

        # Add the chatbot's response to the conversation history
        self.messages.append({"role": "system", "content": content})

        return content
