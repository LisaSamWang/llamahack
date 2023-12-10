import gradio as gr
import requests

url = "http://localhost:8000/chat"


def send_message(message, history):
    form_data = {
        "prompt": message
    }
    response = requests.post(url, data=form_data)
    return response.json()["response"]


gr.ChatInterface(
    send_message,
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Ask me anything about the trial", container=False, scale=7),
    title="Mr. Testimony",
    description="Ask Mr. Testimony any question",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch(share=True)
