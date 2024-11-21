"""Setup project configuration to get environment keys."""

import os

from dotenv import load_dotenv


def setup_huggingface_config():
    from huggingface_hub import login

    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
    login(token=huggingface_token)


def setup_app_config():
    load_dotenv()
    setup_huggingface_config()
