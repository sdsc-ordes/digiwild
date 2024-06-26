from flask import Flask, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

def run_gradio():
    subprocess.Popen(["python3", "gradio_interface.py"])

if __name__ == "__main__":
    run_gradio()
    app.run(host="0.0.0.0", port=8080)  # Set host to 0.0.0.0 to listen on all interfaces


# from flask import Flask, send_from_directory
# import threading
# import gradio_interface  # Import the renamed Gradio interface script

# app = Flask(__name__)

# @app.route('/')
# def serve_index():
#     return send_from_directory('.', 'index.html')

# def run_gradio():
#     gradio_interface.iface.launch(server_name="0.0.0.0", inbrowser=False, share=True)  # Launch Gradio without auto-opening a browser tab

# if __name__ == "__main__":
#     threading.Thread(target=run_gradio).start()
#     app.run(host="0.0.0.0", port=8081)  # Set host to 0.0.0.0 to listen on all interfaces
