import gradio as gr
import requests

url = "http://localhost:8000"


def send_message(message, history):
    print("sending message")
    form_data = {
        "prompt": message
    }
    response = requests.post(url + "/chat", data=form_data)
    return response.json()["response"]


def submit_audio(audio_data):
    print("submitting audio")
    form_data = {
        "audio": audio_data
    }
    response = requests.post(url + "/uploadaudio", data=form_data)
    return response.text


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown(
                """
                # Mr. Testimony
                """)
            audio_upload = gr.Audio(sources="upload", label="Upload Audio File")
            submit_buttom = gr.Button(value="Submit")
            submit_buttom.click(submit_audio, inputs=audio_upload, outputs=[], show_progress=True)
            chat = gr.ChatInterface(
                send_message,
                chatbot=gr.Chatbot(height=500, render=False),
                textbox=gr.Textbox(placeholder="Ask me anything about the trial", container=False, scale=7, render=False),
                description="Ask Mr. Testimony any question about your audio clip and he will answer it to the best of his ability.",
                theme="soft",
                examples=["Did Trump inflate his financial siatuation?"],
                cache_examples=True,
                retry_btn=None,
                undo_btn="Delete Previous",
                clear_btn="Clear",
            )
# Launch the app
url_info = demo.launch(share=True)
time.sleep(5)
with open('gradio_url.txt', 'w') as file:
    file.write(url_info["url"])  # Write the main URL
