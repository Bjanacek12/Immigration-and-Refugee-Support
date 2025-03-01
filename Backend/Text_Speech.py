from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "Audio_Output/speech.mp3"

def Text_Speech(FinalOut):
    # Create the speech audio
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=FinalOut,
    )

    # Save the response content to a file
    response.write_to_file(speech_file_path)