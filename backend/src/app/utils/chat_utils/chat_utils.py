"""Chat utils module containing the chatbot class and model pipeline."""

import os
from typing import Optional

from app.schemas.chat_schemas import TextInput
from transformers import pipeline


# Set up the model
def get_pipeline() -> pipeline:
    """Get the model pipeline for the chatbot."""
    # Load the model pipeline
    model_id = "meta-llama/Llama-3.2-1B-Instruct"
    # Path to the local model
    local_model_path = "/app/backend/models/Llama-3.2-1B-Instruct"

    try:
        # Try using the remote Hugging Face model
        print(f"Attempting to load remote model: {model_id}")
        return pipeline(
            task="text-generation",
            model=model_id,
            torch_dtype="bfloat16",
            device_map="auto",
        )
    except Exception as e:  # pylint: disable=C0103, W0718
        # Log the error for debugging
        print(f"Failed to load remote model: {e}")

        # Attempt to use the local model
        if os.path.exists(local_model_path):
            print(f"Falling back to local model from: {local_model_path}")
            try:
                return pipeline(
                    task="text-generation",
                    model=local_model_path,
                    torch_dtype="bfloat16",
                    device_map="auto",
                )
            except Exception as ex:  # Handle any error when loading the local model
                print(f"Error loading local model: {ex}")
                raise RuntimeError(
                    f"Failed to load the local model. Ensure the model exists at {local_model_path} and is valid."
                ) from ex
        else:
            # Raise an error if the local model is not found, chaining the original remote loading error
            raise RuntimeError(
                f"Failed to load both remote and local models. Ensure the local model exists at {local_model_path}."
            ) from e


# Chat memory storage for all users
chat_memory_per_user: dict = {}


def get_user_chat_memory(
    user_id: str,
    system_message: str = "I'm a helpful assistent",
) -> list:
    """Get the chat memory for the given user ID."""
    if user_id in chat_memory_per_user:
        return chat_memory_per_user[user_id]
    new_memory: list = [{"role": "system", "content": system_message}]
    chat_memory_per_user[user_id] = new_memory
    return new_memory


# Create the chatbot class
class Chatbot:
    """A chatbot that generates responses based on a given model pipeline."""

    def __init__(
        self,
        model_pipeline: pipeline = None,
        user_id: Optional[str] = None,
        system_message: str = "You are a pirate chatbot who always responds in pirate speak!",
        max_history_tokens: int = 1024,
    ) -> None:
        # Use provided pipeline or initialize a default one
        self.pipe = model_pipeline or get_pipeline()
        self.user_id = user_id or "default"
        self.messages = get_user_chat_memory(self.user_id, system_message)
        self.max_history_tokens = max_history_tokens

    def generate_response(self, user_message: TextInput, max_new_tokens: int = 512) -> str:
        """Generate a response to a user message."""
        # Add the user's message to the conversation history
        self.messages.append({"role": "user", "content": user_message.text})

        # Check if we need to trim the conversation history
        input_for_model = self.messages[-self.max_history_tokens :]  # noqa: E203

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

        except Exception as e:  # pylint: disable=C0103
            raise RuntimeError("Error generating chatbot response") from e

        # Add the chatbot's response to the conversation history
        self.messages.append({"role": "system", "content": content})

        return content
