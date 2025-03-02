from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = "/Users/antonytomy/Desktop/Immigration-and-Refugee-Support/Audio_Output/response.mp3"

def text_speech(FinalOut):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=FinalOut,
    )

    response.write_to_file(speech_file_path)