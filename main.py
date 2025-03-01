from fastapi import FastAPI
from pydantic import BaseModel
# from Speech-Text import ask_gpt

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    new_conversation: bool = False

@app.post("/ask")
def ask_gpt_api(request: QueryRequest):
    """
    FastAPI endpoint that sends a query to the GPT handler.
    """
    response = ask_gpt(request.query, request.new_conversation)
    return {"response": response}

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}
