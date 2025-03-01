import openai
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
openai.api_key = API_KEY
THREAD_FILE = "thread.txt"

def chat_with_legalgpt(query, new_conversation=False):

    # If new conversation is requested, remove old thread ID
    if new_conversation and os.path.exists(THREAD_FILE):
        os.remove(THREAD_FILE)

    # Load existing thread ID or create a new one
    thread_id = None
    if os.path.exists(THREAD_FILE):
        with open(THREAD_FILE, "r") as file:
            thread_id = file.read().strip()

    if not thread_id:
        thread = openai.beta.threads.create()
        thread_id = thread.id
        with open(THREAD_FILE, "w") as file:
            file.write(thread_id)

    # Set unique filename based on thread ID
    conversation_log = f"conversation_{thread_id}.txt"

    # Send query to assistant
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=query
    )

    # Run assistant and wait for response
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=ASSISTANT_ID
    )

    while run.status in ["queued", "in_progress"]:
        time.sleep(1)
        run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

    # Retrieve assistant response
    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    assistant_reply = messages.data[0].content[0].text.value

    # Save query and response to a thread-specific file
    with open(conversation_log, "a") as log_file:
        log_file.write(f"\nUser: {query}\nAssistant: {assistant_reply}\n{'-'*40}\n")

    return assistant_reply

# Example Usage
query = input("You: ")
response = chat_with_legalgpt(query, new_conversation=False)  # Set to True for a new chat
print("Assistant:", response)