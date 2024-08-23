import gradio as gr
import os
from utils_visible import set_visible

PATH = os.getcwd()
CAUSE_COL_WIDTH = "50px"

def show_causes(choice): 
    visible = set_visible(choice)
    button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_causes(visible)
    return button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2

def create_causes(visible):
    button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause = create_causes_buttons(visible)      
    dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_causes_dropdown(visible)
    return button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2


def create_causes_buttons(visible): 
    with gr.Row() as image_row:
            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_collision = gr.Button("Collision with a means of transport", 
                                             visible=visible,
                                             icon=PATH + '/assets/logos/van.png',
                                             elem_id="buttons-conditions")
                
            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_deliberate_destruction = gr.Button("Destruction / Deliberatly removed", 
                                                          icon=PATH + '/assets/logos/destruction.png',
                                                          visible=visible,
                                                          elem_id="buttons-conditions")
 
            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_indirect_destruction = gr.Button("Indirect destruction", 
                                                        icon=PATH + '/assets/logos/indirect.png',
                                                        visible=visible,
                                                        elem_id="buttons-conditions")

            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_natural_cause = gr.Button("Natural cause", 
                                                 icon=PATH + '/assets/logos/natural.png', 
                                                 visible=visible,
                                                 elem_id="buttons-conditions")
    return button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause

def create_causes_dropdown(visible):
    with gr.Row() as dropdown_row:
        dropdown = gr.Dropdown(choices=[], 
                               label="Choices will appear here...",
                               visible=visible, interactive=False, elem_id="dropdown-conditions")
    openfield_level2 = gr.Textbox(visible=False, elem_id="dropdown-conditions")
    dropdown_level2 = gr.Dropdown(choices=[], visible=False, elem_id="dropdown-conditions")
    dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False, elem_id="dropdown-conditions")
    return dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2


     