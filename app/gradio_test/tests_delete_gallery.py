import gradio as gr

# Example initial image list
images = [
    "https://via.placeholder.com/150/0000FF",
    "https://via.placeholder.com/150/FF0000",
    "https://via.placeholder.com/150/00FF00"
]

# Function to remove a selected image from the gallery
def delete_image(selected_image, image_list):
    if selected_image in image_list:
        image_list.remove(selected_image)  # Remove the selected image
    return image_list  # Return the updated image list

# Gradio app
with gr.Blocks() as demo:
    gallery = gr.Gallery(value=images, label="Gallery")  # Gallery of images
    selected_image = gr.Dropdown(choices=images, label="Select Image to Delete")  # Dropdown for selection
    delete_button = gr.Button("Delete Selected Image")  # Button to delete
    
    # When button is clicked, delete the selected image and update gallery
    delete_button.click(fn=delete_image, inputs=[selected_image, gallery], outputs=gallery)
    
demo.launch(server_name="0.0.0.0", server_port=3232)