import gradio as gr
from gradio_modal import Modal
import numpy as np
from maps import get_location
from utils_json import *

     
def save_input(input, df):
    #input_value = str(input)
    df_values = np.array(df) # handle empty dataframe case
    new_row = [input, 0, input]  # default 'age' as 0 for now
    df_values = np.vstack([df_values, new_row])
    df = gr.DataFrame(value=df_values)
    return df

with gr.Blocks() as demo:
    # with gr.Tab("Tab 1"):
    show_btn = gr.Button("Show Modal")
    df = gr.Dataframe(
        headers=["image", "location"],
        #datatype=["str", "number", "str"],
        row_count=1,
        #col_count=(3, "fixed"),
    )
    show_markdown = gr.Markdown("This is a markdown")
    with Modal(visible=False) as modal:
        input = gr.Textbox(label="Input 1", interactive=True)
        # ---------------------------------------------------------
        # Intro Text
        with gr.Row():
            with gr.Column(scale=1):
                title = gr.Markdown("# Welcome to Digiwild", label="Title")
                description = gr.Markdown("Please record your wildlife observations here !", label="description")

        # ---------------------------------------------------------
        # Camera
        with gr.Row():
            #with gr.Column(scale=1):
            camera = gr.Image(elem_id="image")
                
        # ---------------------------------------------------------
        # Location
        #with gr.Row():
            with gr.Column(scale=1):
                location = gr.Textbox(visible=True, interactive=True, label="Location of Sighting")
                #display location processing
                identified_location= gr.Textbox(visible=False, interactive=False, 
                                                label="Identified GPS Location")
                with gr.Row():
                    #to clear it
                    clear_location = gr.ClearButton(components=[location], visible=True, interactive=True, scale=1
                                                    )
                    clear_location.click()
                    #to submit it
                    submit_location = gr.Button("Get GPS Coordinates", visible=True, interactive=True, scale=3)
                    submit_location.click(get_location, inputs=[location], outputs=[identified_location])
        
        # ---------------------------------------------------------
        
        button = gr.Button("Click me")
        button.click(save_input, 
                        inputs=[input, df],
                        outputs=[df])
        button.click(lambda: Modal(visible=False), None, modal)
    show_btn.click(lambda: Modal(visible=True), None, modal)
    show_btn.click(create_json)


     
     
     
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3333)