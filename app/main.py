import gradio as gr
from functools import partial
from dead import show_section_dead
from wounded import show_section_wounded
from dropdowns import *
from maps import get_location
from style import *

with gr.Blocks() as demo:
    # ---------------------------------------------------------
    # Intro Text
    with gr.Row():
        with gr.Column(scale=1):
            title = gr.Markdown("# Welcome to Digiwild", label="Title")
            description = gr.Markdown("Lorem ipsum", label="description")

    # ---------------------------------------------------------
    # Camera
    with gr.Row():
        with gr.Column(scale=1):
            camera = gr.Image()
            
    # ---------------------------------------------------------
    # Location
    with gr.Row():
        with gr.Column(scale=1):
            location = gr.Textbox(visible=True, interactive=True, label="Location of Sighting")
            #display location processing
            identified_location= gr.Textbox(visible=False, interactive=False, 
                                            label="Identified GPS Location")
            with gr.Row():
                #to clear it
                clear_location = gr.ClearButton(components=[location], visible=True, interactive=True, 
                                                #elem_classes=["custom-button"]
                                                )
                clear_location.click()
                #to submit it
                submit_location = gr.Button("Submit", visible=True, interactive=True)
                submit_location.click(get_location, inputs=[location], outputs=[identified_location])
            

    # ---------------------------------------------------------
    # Dead and Wounded Buttons
    with gr.Row() as block_form:
        with gr.Column(scale=1):
            butt_dead = gr.Button("Dead")

        with gr.Column(scale=1):
            butt_wounded = gr.Button("Wounded")

    # ---------------------------------------------------------
    # Initiate sections
    section_dead, button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead = show_section_dead(False)
    section_wounded, button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded= show_section_wounded(False)

    # ---------------------------------------------------------
    # Dead Button Logic
    partial_show_section_dead = partial(show_section_dead, True)
    partial_hide_section_wounded = partial(show_section_wounded, False)
    butt_dead.click(partial_show_section_dead, inputs=None, outputs=[section_dead, 
                                                                     button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                                                     dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead
                                                                     ])
    butt_dead.click(partial_hide_section_wounded, inputs=None, outputs=[section_wounded, 
                                                                        button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                                                        dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded
                                                                        ])
    # ---------------------------------------------------------
    # Wounded Button Logic
    partial_show_section_wounded = partial(show_section_wounded, True)
    partial_hide_section_dead = partial(show_section_dead, False)
    butt_wounded.click(partial_show_section_wounded, inputs=None, outputs=[section_wounded, 
                                                                        button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                                                        dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded
                                                                        ])
    butt_wounded.click(partial_hide_section_dead, inputs=None, outputs=[section_dead, 
                                                                        button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                                                        dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead
                                                                        ])
    # ---------------------------------------------------------
    # Dropdowns Dead
    button_collision_dead.click(dropdown_collision,  
                                outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
    button_deliberate_destruction_dead.click(dropdown_deliberate_destruction, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
    button_indirect_destruction_dead.click(dropdown_indirect_destruction, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
    button_natural_cause_dead.click(dropdown_natural_cause, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])

    dropdown_dead.select(on_select, None, [dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])

    # ---------------------------------------------------------
    # Dropdowns Wounded
    button_collision_wounded.click(dropdown_collision,  
                                outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    button_deliberate_destruction_wounded.click(dropdown_deliberate_destruction, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    button_indirect_destruction_wounded.click(dropdown_indirect_destruction, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    button_natural_cause_wounded.click(dropdown_natural_cause, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    
    dropdown_wounded.select(on_select, None, [dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])

    # ---------------------------------------------------------
    #Follow up Events

    # ---------------------------------------------------------
    #Submit Button
    with gr.Column(scale=1):
        subbutt = gr.Button("Submit")
        output_message = gr.Markdown("Thank you, you didn't save this one but you could save the next")

    

demo.launch(server_name="0.0.0.0")