import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form, File, Annotated
from llmQuery import get_llm_result
from speech_to_text import convert_speech_to_text
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


@app.post("/uploadaudio")
async def upload_video(audio: Annotated[bytes, File()]):
    if not audio:
        return {"message": "No file sent"}
    else:
        transcript = convert_speech_to_text(audio)
        return {"file_size": len(audio)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
