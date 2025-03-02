import os
from Analysis import legalgpt
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speech_text(AudioPath):
    audio_file_path = AudioPath
    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file, 
        response_format="json"
    )

    transcribed_text = transcription.text
    
    return transcribed_text


