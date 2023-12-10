import openai
import pymongo
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
app = FastAPI()

load_dotenv()


@app.get("/")
def read_root(request: Request):
    return {"message": "Welcome to the Mental Health Chatbot API!"}


@app.post("/chat")
def process_prompt(prompt: str = Form(...)):
    print(prompt)
    return {"response": 'Hello'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
