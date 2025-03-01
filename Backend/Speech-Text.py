import os
from Analysis import analyze

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file_path = "Audios_Input/Test1.m4a"
audio_file = open(audio_file_path, "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="json"
)

# Extract directory from audio file path
directory = os.path.dirname(audio_file_path)
transcription_file_path = os.path.join(directory, "transcription.txt")
transcribed_text = transcription["text"]
# Save transcription to a file
with open(transcription_file_path, "w") as transcription_file:
    transcription_file.write(transcribed_text)

print(f"Transcription saved to {transcription_file_path}")
print(transcription['text'])

analyze(transcription['text'])