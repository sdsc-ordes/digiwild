import gradio as gr

def get_location(coordinates):
    return coordinates

def launch_gradio():
    with gr.Blocks() as iface:
        # Create button and text box
        button = gr.Button("Check Coordinates", elem_id="check-coordinates-button")
        textbox = gr.Textbox(label="Coordinates", interactive=False, elem_id="coordinates-box")
        
        # Custom HTML and JavaScript
        custom_js = """
                function getCoordinates() {
                    navigator.geolocation.getCurrentPosition(function(position) {
                        const latitude = position.coords.latitude;
                        const longitude = position.coords.longitude;
                        const coordinates = `Latitude: ${latitude}, Longitude: ${longitude}`;
                        
                        // Send coordinates back to Gradio
                        document.getElementById("coordinates-box").value = coordinates;
                    });
                }
                
                document.getElementById("check-coordinates-button").onclick = getCoordinates;
        """

        # Add the HTML component
        html_component = gr.HTML(value=custom_js)

        button.click(js=custom_js)

        iface.launch(inbrowser=False, server_name="0.0.0.0")

if __name__ == "__main__":
    launch_gradio()



# import gradio as gr

# def get_location():
#     return "Waiting for coordinates..."

# def launch_gradio():
#     with gr.Blocks() as iface:
#         # Create button and text box
#         button = gr.Button("Check Coordinates", elem_id="check-coordinates-button")
#         textbox = gr.Textbox(label="Coordinates", interactive=False, elem_id="coordinates-box")
        
#         # Custom HTML and JavaScript
#         custom_js = """
#             function getCoordinates() {
#                 navigator.geolocation.getCurrentPosition(function(position) {
#                     const latitude = position.coords.latitude;
#                     const longitude = position.coords.longitude;
#                     const coordinates = `Latitude: ${latitude}, Longitude: ${longitude}`;
                    
#                     // Send coordinates back to Gradio
#                     return coordinates
#                 });

#             }
#         """

#         # Add the HTML component
#         html_component = gr.HTML(value=custom_js)
        
#         # Define a JS function to send the button click message
#         button.click(None, [], [], js=custom_js)

#         # Update the textbox when coordinates are received
#         iface.load(
#             lambda data: gr.update(textbox, value=data),
#             inputs=[],
#             outputs=[textbox],
#             js=custom_js
#         )

#     iface.launch(inbrowser=False, server_name="0.0.0.0")

# if __name__ == "__main__":
#     launch_gradio()

