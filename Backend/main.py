from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
from Analysis import legalgpt  # Handles GPT queries
from Speech_Text import speech_text  # Converts speech to text
from TextSpeech import Text_Speech  # Converts text to speech

app = FastAPI()
UPLOAD_FOLDER = "Audio_Output"
OUTPUT_FOLDER = "Audio_Input"

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
 
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    speech_text_result = speech_text(file_path)
    gpt_response = legalgpt(speech_text_result, new_conversation=False)

    output_audio_path = os.path.join(OUTPUT_FOLDER, "response.mp3")
    Text_Speech(gpt_response, output_audio_path)

    # Return JSON + MP3 file
    return JSONResponse(
        content={
            "query_text": speech_text_result,  # Extracted text from audio
            "gpt_response": gpt_response,  # LegalGPT output
            "audio_output_url": "/download-audio"  # URL to download MP3
        }
    )

@app.get("/download-audio")
async def download_audio():
    """
    Returns the generated MP3 file.
    """
    output_audio_path = os.path.join(OUTPUT_FOLDER, "response.mp3")
    return FileResponse(output_audio_path, media_type="audio/mpeg", filename="response.mp3")

@app.get("/")
def root():
    """
    Root endpoint to check API status.
    """
    return {"message": "FastAPI is running!"}
