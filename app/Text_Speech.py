import os
from pathlib import Path
from openai import OpenAI

client = OpenAI()

def text_speech(FinalOut):

    output_audio_dir = os.path.join(os.getcwd(), "app", "Audio_Output")
    output_audio_path = os.path.join(output_audio_dir, "response.mp3")

   
    os.makedirs(output_audio_dir, exist_ok=True)

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=FinalOut,
    )

    response.write_to_file(output_audio_path)
