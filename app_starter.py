import subprocess
import signal
import sys
import webbrowser
import time

def start_backend():
    return subprocess.Popen(["python3", "main.py"])

def start_ui():
    return subprocess.Popen(["python3", "chatui.py"])

def open_gradio_url():
    while True:
        try:
            with open('gradio_url.txt', 'r') as file:
                url = file.read().strip()
                if url:
                    webbrowser.open(url)
                    break
        except FileNotFoundError:
            pass
        time.sleep(1)  # Check every 1 second

def signal_handler(sig, frame):
    print("Shutting down...")
    backend_process.terminate()
    ui_process.terminate()
    sys.exit(0)

if __name__ == '__main__':
    print("Starting Mr. Testimony...")
    backend_process = start_backend()
    print("Backend started. Starting UI...")
    ui_process = start_ui()

    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Open Gradio URL
    open_gradio_url()

    # Wait for the child processes to terminate
    backend_process.wait()
    ui_process.wait()
