import os
from pathlib import Path
from openai import OpenAI

client = OpenAI()

OUTPUT_FOLDER = Path(__file__).parent / "Audio_Output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

speech_file_path = OUTPUT_FOLDER / "response.mp3"

def text_speech(FinalOut):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=FinalOut,
    )

    response.write_to_file(speech_file_path)
