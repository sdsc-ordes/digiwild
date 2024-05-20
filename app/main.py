import gradio as gr
from functools import partial
from dead import show_section_dead
from wounded import show_section_wounded
from dropdowns import *

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
    section_dead, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown = show_section_dead(False)
    section_wounded, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown = show_section_wounded(False)

    # Dead Button Logic
    partial_show_section_dead = partial(show_section_dead, True)
    partial_hide_section_wounded = partial(show_section_wounded, False)
    butt_dead.click(partial_show_section_dead, inputs=None, outputs=[section_dead, 
                                                                     button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, 
                                                                     dropdown])
    butt_dead.click(partial_hide_section_wounded, inputs=None, outputs=[section_wounded, 
                                                                        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, 
                                                                        dropdown])

    # Wounded Button Logic
    partial_show_section_wounded = partial(show_section_wounded, True)
    partial_hide_section_dead = partial(show_section_dead, False)
    butt_wounded.click(partial_show_section_wounded, inputs=None, outputs=[section_wounded, 
                                                                        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, 
                                                                        dropdown])
    butt_wounded.click(partial_hide_section_dead, inputs=None, outputs=[section_dead, 
                                                                        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, 
                                                                        dropdown])

    # Dropdowns 
    button_collision.click(dropdown_collision, outputs=dropdown)
    button_deliberate_destruction.click(dropdown_deliberate_destruction, outputs=dropdown)
    button_indirect_destruction.click(dropdown_indirect_destruction, outputs=dropdown)
    button_natural_cause.click(dropdown_natural_cause, outputs=dropdown)
    

    with gr.Column(scale=1):
        subbutt = gr.Button("Submit")
        output_message = gr.Markdown("Thank you, you didn't save this one but you could save the next")

    

demo.launch(server_name="0.0.0.0")