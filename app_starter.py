import subprocess

def start_backend():
    subprocess.Popen(["python3", "main.py"])

def start_ui():
    subprocess.Popen(["python3", "chatui.py"])

if __name__ == '__main__':
    print("Starting Mr. Testimony...")
    start_backend()
    print("Backend started. Starting UI...")
    start_ui()
