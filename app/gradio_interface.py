import gradio as gr

def get_location():
    return "Waiting for coordinates..."

def launch_gradio():
    with gr.Blocks() as iface:
        button = gr.Button("Check Coordinates", elem_id="check-coordinates-button")
        textbox = gr.Textbox(label="Coordinates", interactive=False, elem_id="coordinates-box")
        
        button.click(None, [], [], js="parent.postMessage('button_clicked', '*');")
        
        iface.load(
            lambda data: gr.update(textbox, value=data),
            inputs=[],
            outputs=[textbox],
            js="window.addEventListener('message', function(event) { if (event.data.latitude && event.data.longitude) { window.gradio_handle(event.data); } });"
        )

    iface.launch(inbrowser=False, server_name="0.0.0.0")

if __name__ == "__main__":
    launch_gradio()



# import gradio as gr

# def get_location(latitude, longitude):
#     return f"Latitude: {latitude}, Longitude: {longitude}"

# def launch_gradio():
#     iface = gr.Interface(
#         fn=get_location,
#         inputs=["number", "number"],
#         outputs="text",
#         live=True,
#         description="Enter your GPS coordinates."
#     )
#     iface.launch(inbrowser=False) #server_name="0.0.0.0"

# if __name__ == "__main__":
#     launch_gradio()
