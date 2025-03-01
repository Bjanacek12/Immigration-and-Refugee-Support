import openai
import os
from Analysis import analyze

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file_path = "Audios_Input/Test1.m4a"
audio_file = open(audio_file_path, "rb")
transcription = openai.Audio.transcribe(
    model="whisper-1", 
    file=audio_file,
)

# Extract directory from audio file path
directory = os.path.dirname(audio_file_path)
transcription_file_path = os.path.join(directory, "transcription.txt")

# Save transcription to a file
with open(transcription_file_path, "w") as transcription_file:
    transcription_file.write(transcription['text'])

print(f"Transcription saved to {transcription_file_path}")
print(transcription['text'])