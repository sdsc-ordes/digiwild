import gradio as gr
import os

PATH = os.getcwd()

def create_top_section(visible): 
    with gr.Row() as image_row:
            with gr.Column(scale=1, min_width="50px"):
                img1 = gr.Image(value=PATH + '/assets/logos/van.png', show_download_button=False, show_label=False, height="150px")
                button_collision = gr.Button("Collision with a means of transport", visible=visible, elem_id="warning", elem_classes=".feedback")
                
            with gr.Column(scale=1, min_width="50px"):
                img2 = gr.Image(value=PATH + '/assets/logos/destruction.png', show_download_button=False, show_label=False, height="150px")
                button_deliberate_destruction = gr.Button("Destruction / Deliberatly removed", visible=visible)
 
            with gr.Column(scale=1, min_width="50px"):
                img3 = gr.Image(value=PATH + '/assets/logos/indirect.png', show_download_button=False, show_label=False, height="150px")
                button_indirect_destruction = gr.Button("Indirect destruction", visible=visible)

            with gr.Column(scale=1, min_width="50px"):
                img4 = gr.Image(value=PATH + '/assets/logos/natural.png', show_download_button=False, show_label=False, height="150px")
                button_natural_cause = gr.Button("Natural cause", visible=visible)
    return image_row, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause

def create_dropdown(visible):
    print(visible)
    with gr.Row() as dropdown_row:
        dropdown = gr.Dropdown(choices=[], label="Dropdown", interactive=True, visible=visible)
    openfield_level2 = gr.Textbox(visible=False)
    dropdown_level2 = gr.Dropdown(choices=[], visible=False)
    dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False)
    return dropdown_row, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2


     