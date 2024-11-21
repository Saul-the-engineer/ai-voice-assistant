"""This module contains the speech to text service for the API."""

import os

import whisper
from app.utils.file_utils import (
    create_unique_tmp_file,
    persist_binary_file_locally,
)


def convert_file_to_readable_mp3(local_input_file_path: str, local_output_file_path: str):
    os.system(f"ffmpeg -i {local_input_file_path} {local_output_file_path}")


def convert_audio_to_text(model: whisper.Whisper, file_path: str) -> str:
    """Transcribe the audio at the given file path using the Whisper model."""
    result = model.transcribe(file_path)
    return result["text"]


def __get_transcoded_audio_file_path(data: bytes) -> str:
    local_file_path = persist_binary_file_locally(data, file_suffix="user_audio.mp3")
    local_output_file_path = create_unique_tmp_file(file_suffix="transcoded_user_audio.mp3")
    convert_file_to_readable_mp3(local_input_file_path=local_file_path, local_output_file_path=local_output_file_path)

    return local_output_file_path


async def handle_audio_from_user(model: whisper.Whisper, file: bytes) -> str:
    """
        Entrypoint
    :param file:
    :return:
    """
    print("handle audio from user")
    transcoded_user_audio_file_path = __get_transcoded_audio_file_path(file)
    transcript_content_text = convert_audio_to_text(
        model=model,
        file_path=transcoded_user_audio_file_path,
    )
    return transcript_content_text
    # ai_text_reply = handle_get_response_for_user(text_content)
    # generated_audio_ai = convert_text_to_audio(ai_text_reply)
    # output_audio_local_file_path = persist_binary_file_locally(
    #     data=generated_audio_ai['AudioStream'].read(),
    #     file_suffix='ai_audio_reply.mp3'
    # )

    # return output_audio_local_file_path
    #     file_suffix='ai_audio_reply.mp3'
    # )

    # return output_audio_local_file_path
