from flask import Flask, request, jsonify, send_file
import os
import shutil
from app.Analysis import legalgpt
from app.Speech_Text import speech_text
from app.Text_Speech import text_speech
from flask_cors import CORS 



app = Flask(__name__)

new_conversation=False
CORS(app)

UPLOAD_FOLDER = "Audio_Input"
OUTPUT_FOLDER = "Audio_Output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

#processing input audio and getting legal advice as text and audio
@app.route("/process-audio/", methods=["POST"])
def process_audio():    
    global new_conversation
    #checking for errors
    # Check if file is in request
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    #empty file
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    
    # saving speech file to audio input folder
    file_path = os.path.join("Audio_Input", file.filename)
    file.save(file_path)

    # converting speech to text and saving output
    speech_text_result = speech_text(file_path)

    # getting custom gpt response()
    gpt_response = legalgpt(speech_text_result, new_conversation)

    #staying in same convo
    new_conversation=False

    # converting response from gpt to speech
    text_speech(gpt_response)

    # returning query and output from AI model
    return jsonify({
        "query_text": speech_text_result,
        "gpt_response": gpt_response,
    })

#getting audio legal advice
@app.route("/download-audio", methods=["GET"])
def download_audio():
    output_audio_path = os.path.join("Audio_Output", "response.mp3")
    #if audio file path exists then sending it or else giving error msg
    if os.path.exists(output_audio_path):
        return send_file(output_audio_path, mimetype="audio/mpeg", as_attachment=True, download_name="response.mp3")
    else:
        return jsonify({"error": "audio file not found"}), 404
 
#starting new conversation with model
@app.route("/set-new-conversation", methods=["POST"])
def set_new_conversation():
    global new_conversation
    new_conversation = True
    return jsonify({"message": "new conversation being starting"})


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "LegalGPT is running..."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080
    app.run(host="0.0.0.0", port=port)




