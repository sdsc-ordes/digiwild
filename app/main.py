import gradio as gr
from functools import partial

def truck_dropdown():
    return gr.Dropdown(choices=["Road vehicle", "Train", "Aircraft", "Boat", "Other", "Unknown"], label="Collision with a means of transport", interactive=True)

def truckb_dropdown():
    return gr.Dropdown(choices=["Hunting", "Trap", "Poisoning", "Removal or direct capture", "Fishing", "Other", "Unkown"], label="Destruction / Deliberatly removed", interactive=True)        

def show_section_dead(visible):
    with gr.Column(visible=visible) as section_dead:
        gr.Markdown("# Dead")
        gr.Markdown("Please describe the cause of death")
        with gr.Row():
            with gr.Column(scale=1, min_width="100px"):
                img1 = gr.Image(value='./assets/van.png', show_download_button=False, show_label=False)
                butt1 = gr.Button("Collision with a means of transport", visible=visible)
                
            with gr.Column(scale=1, min_width="100px"):
                img1 = gr.Image(value='./assets/destruction.png', show_download_button=False, show_label=False)
                butt2 = gr.Button("Destruction / Deliberatly removed", visible=visible)
                

        with gr.Row():
            with gr.Column(scale=1, min_width="100px"):
                img3 = gr.Image(value='./assets/indirect.png', show_download_button=False, show_label=False)
                butt3 = gr.Button("Indirect destruction", visible=visible)

            with gr.Column(scale=1, min_width="100px"):
                img4 = gr.Image(value='./assets/natural.png', show_download_button=False, show_label=False)
                butt4 = gr.Button("Natural cause", visible=visible)

                
        with gr.Row():
            dropdown = gr.Dropdown(choices=[], label="Dropdown", interactive=True, visible=visible)

    return section_dead, butt1, butt2, butt3, butt4, dropdown

def show_section_wounded(visible):
    #with gr.Tab("Wounded Information"):
    with gr.Column(visible=visible) as wounded_section:
        gr.Markdown("# Please describe the cause of wound")

        with gr.Row():
            with gr.Column(scale=1, min_width="100px"):
                img1 = gr.Image(value='./assets/van.png', show_download_button=False, show_label=False)
                butt1 = gr.Button("Collision with a means of transport")
                
            with gr.Column(scale=1, min_width="100px"):
                img1 = gr.Image(value='./assets/destruction.png', show_download_button=False, show_label=False)
                butt2 = gr.Button("Destruction / Deliberatly removed")

        with gr.Row():
            with gr.Column(scale=1, min_width="100px"):
                img3 = gr.Image(value='./assets/indirect.png', show_download_button=False, show_label=False)
                butt3 = gr.Button("Indirect destruction")
                
            with gr.Column(scale=1, min_width="100px"):
                img4 = gr.Image(value='./assets/natural.png', show_download_button=False, show_label=False)
                butt4 = gr.Button("Natural cause")

                
        with gr.Row():
            dropdown = gr.Dropdown(choices=[], label="Dropdown", interactive=True)

    # Change variables and names
    return wounded_section





with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            title = gr.Markdown("# Welcome to Digiwild", label="Title")
            description = gr.Markdown("Lorem ipsum", label="description")

    with gr.Row():
        with gr.Column(scale=1):
            camera = gr.Image()

    with gr.Row() as block_form:
        with gr.Column(scale=1):
            butt_dead = gr.Button("Dead")

        with gr.Column(scale=1):
            butt_wounded = gr.Button("Wounded")

    # Initiate sections
    section_dead, butt1, butt2, butt3, butt4, dropdown = show_section_dead(False)
    section_wounded = show_section_wounded(False)

    # Dead Button Logic
    partial_show_section_dead = partial(show_section_dead, True)
    partial_hide_section_wounded = partial(show_section_wounded, False)
    butt_dead.click(partial_show_section_dead, inputs=None, outputs=[section_dead, butt1, butt2, butt3, butt4, dropdown])
    butt_dead.click(partial_hide_section_wounded, inputs=None, outputs=section_wounded)

    # Wounded Button Logic
    partial_show_section_wounded = partial(show_section_wounded, True)
    partial_hide_section_dead = partial(show_section_dead, False)
    butt_wounded.click(partial_show_section_wounded, inputs=None, outputs=section_wounded)
    butt_wounded.click(partial_hide_section_dead, inputs=None, outputs=[section_dead, butt1, butt2, butt3, butt4, dropdown])

    butt1.click(truck_dropdown, outputs=dropdown)
    butt2.click(truckb_dropdown, outputs=dropdown)
    # section_dead.

    with gr.Column(scale=1):
        subbutt = gr.Button("Submit")
        output_message = gr.Markdown("Thank you, you didn't save this one but you could save the next")

    

demo.launch(server_name="0.0.0.0")