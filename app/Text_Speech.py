import os
from pathlib import Path
from openai import OpenAI

client = OpenAI()


if not os.path.exists("Audio_Output"):
    os.makedirs("Audio_Output")

def text_speech(FinalOut):
    speech_file_path = "Audio_Output/response.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=FinalOut,
    )

    response.write_to_file(speech_file_path)
