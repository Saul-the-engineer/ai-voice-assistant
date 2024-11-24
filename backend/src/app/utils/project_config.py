"""Setup project configuration to get environment keys."""

import os

from dotenv import load_dotenv
from huggingface_hub import login


def setup_huggingface_config():
    """Load Hugging Face credentials from environment variables."""
    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
    login(token=huggingface_token)


def setup_app_config():
    """Load environment variables from the .env file."""
    load_dotenv()
    setup_huggingface_config()
