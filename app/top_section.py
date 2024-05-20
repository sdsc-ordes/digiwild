import gradio as gr

def create_top_section(visible): 
    with gr.Row() as image_row:
            with gr.Column(scale=1, min_width="50px"):
                img1 = gr.Image(value='app/assets/van.png', show_download_button=False, show_label=False)
                button_collision = gr.Button("Collision with a means of transport", visible=visible)
                
            with gr.Column(scale=1, min_width="50px"):
                img2 = gr.Image(value='app/assets/destruction.png', show_download_button=False, show_label=False)
                button_deliberate_destruction = gr.Button("Destruction / Deliberatly removed", visible=visible)
                

        #with gr.Row():
            with gr.Column(scale=1, min_width="50px"):
                img3 = gr.Image(value='app/assets/indirect.png', show_download_button=False, show_label=False)
                button_indirect_destruction = gr.Button("Indirect destruction", visible=visible)

            with gr.Column(scale=1, min_width="50px"):
                img4 = gr.Image(value='app/assets/natural.png', show_download_button=False, show_label=False)
                button_natural_cause = gr.Button("Natural cause", visible=visible)
    return image_row, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause

def create_dropdown(visible):
    with gr.Row() as dropdown_row:
        dropdown = gr.Dropdown(choices=[], label="Dropdown", interactive=True, visible=visible)
    return dropdown_row, dropdown


     