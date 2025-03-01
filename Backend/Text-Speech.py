import requests
import json
from pathlib import Path
from openai import OpenAI

textInfo_URL = ""
textResponse = requests.get(textInfo_URL)
with open(textResponse.json(), "r") as file:
    data = json.load(file)
textInput = json.dumps(data)


client = OpenAI(key)
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model ="tts-1",
    voice ="ash",
    input = textInput,
)
response.stream_to_file(speech_file_path)