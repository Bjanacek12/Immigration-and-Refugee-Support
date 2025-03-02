import openai
import time
import os
import json
from dotenv import load_dotenv, set_key


# load environment variables from .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
THREAD_ID = os.getenv("THREAD_ID")  

openai.api_key = API_KEY


def legalgpt(query, new_conversation=False):
    global THREAD_ID
    
    # getting new thread if for new convo
    if new_conversation or not THREAD_ID:
        thread = openai.beta.threads.create()
        THREAD_ID = thread.id
        set_key(".env", "THREAD_ID", THREAD_ID) 

    

    # getting file path for conversation.txt file
    conversation_log = os.path.join("conversations", f"conversation_{THREAD_ID}.txt")

    # Sending query
    openai.beta.threads.messages.create(
        thread_id=THREAD_ID,
        role="user",
        content=query
    )

    # Run assistant and wait for response
    run = openai.beta.threads.runs.create(
        thread_id=THREAD_ID,
        assistant_id=ASSISTANT_ID
    )

    #getting response from custom GPT fine tuned model from OPENAI(code from documentation)
    while run.status in ["queued", "in_progress"]:
        run = openai.beta.threads.runs.retrieve(thread_id=THREAD_ID, run_id=run.id)

    messages = openai.beta.threads.messages.list(thread_id=THREAD_ID)
    assistant_reply = messages.data[0].content[0].text.value


    # Saving convo to proper thread
    with open(conversation_log, "a") as log_file:
        log_file.write("\nUser: " + query + "\nAssistant: " + assistant_reply + "\n" + "-" * 40 + "\n")

    # save the most recent query and response and output to output.json
    output_data = {
        "thread_id": THREAD_ID,
        "query": query,
        "response": assistant_reply
    }
    with open("output.json", "w") as json_file:
        json.dump(output_data, json_file)
        
    return assistant_reply



