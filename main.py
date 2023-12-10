import openai
import pymongo
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from llmQuery import get_llm_result
app = FastAPI()

load_dotenv()


@app.get("/")
def read_root(request: Request):
    return {"message": "Welcome to the Mr. Testimony Chatbot API!"}


@app.post("/chat")
def process_prompt(prompt: str = Form(...)):
    print("Prompt", prompt)
    llm_result = get_llm_result(prompt)
    print("LLM Result", llm_result)
    return {"response": llm_result}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
