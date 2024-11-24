"""Utility functions for working with files."""

import os
import tempfile
from uuid import uuid4

TMP_FOLDER_NAME = "voice_assistant"


def create_secure_tmp_folder():
    """Create a secure temporary folder for storing files."""
    base_tmp_path = tempfile.gettempdir()
    full_path = os.path.join(base_tmp_path, TMP_FOLDER_NAME)
    os.makedirs(full_path, exist_ok=True)
    # Restrict access to this folder, for Unix based systems
    os.chmod(full_path, 0o700)  # Only owner can read, write, and execute
    return full_path


def get_unique_tmp_file_path():
    """Generate a unique temporary file path."""
    return os.path.join(create_secure_tmp_folder(), str(uuid4()))


def create_unique_tmp_file(file_suffix: str):
    """Create a unique temporary file with the given suffix."""
    return f"{get_unique_tmp_file_path()}_{file_suffix}"


def persist_binary_file_locally(data: bytes, file_suffix: str) -> str:
    """Persist the binary data to a temporary file and return the file path."""
    file_path = create_unique_tmp_file(file_suffix)
    with open(file_path, "wb") as f:  # pylint: disable=C0103
        f.write(data)
    # Set file to be readable and writable only by the owner
    os.chmod(file_path, 0o600)
    return file_path


def securely_delete_file(file_path):
    """Overwrite and remove a file to prevent file recovery."""
    if os.path.exists(file_path):
        with open(file_path, "ba+") as file:
            length = file.tell()
            file.seek(0)
            file.write(os.urandom(length))
        os.remove(file_path)
