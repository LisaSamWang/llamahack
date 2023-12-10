import openai
import pymongo
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
app = FastAPI()

load_dotenv()

client = pymongo.MongoClient("<connection-string>")


@app.get("/")
def read_root(request: Request):
    return {"message": "Welcome to the Mental Health Chatbot API!"}


@app.post("/chat")
def process_prompt(prompt: str = Form(...)):
    
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
