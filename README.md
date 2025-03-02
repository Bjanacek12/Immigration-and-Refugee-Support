# Immigration-and-Refugee-Support

### The POST /process-audio/ route allows users to upload an audio file, which is converted to text, processed by LegalGPT for a response, and then converted back into speech. The API returns the transcribed text and the GPT-generated response.

### The GET /download-audio route provides the processed audio response from the /process-audio/ post request as an MP3 file 

## #The POST /set-new-conversation route resets the conversation(refresh button) so that the next /process-audio/ request starts a new conversation 

### The GET / route checks if the API is running and returns a simple status message indicating that the server is active.

