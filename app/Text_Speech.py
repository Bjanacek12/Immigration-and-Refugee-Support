import os
from pathlib import Path
from openai import OpenAI

client = OpenAI()




def text_speech(FinalOut):
    output_audio_dir = os.path.join(os.getcwd(), "app", "Audio_Output")
    output_audio_path = os.path.join(output_audio_dir, "response.mp3")

    if not os.path.exists("Audio_Output"):
        os.makedirs("Audio_Output")
        
    speech_file_path = "Audio_Output/response.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=FinalOut,
    )

    response.write_to_file(speech_file_path)
