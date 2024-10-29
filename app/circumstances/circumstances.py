import gradio as gr
import os
from dotenv import load_dotenv

from utils.utils_visible import set_visible
from validation_submission.add_json import add_data_tmp

load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv('PATH_ASSETS')
LOGO_PATH = PATH + PATH_ASSETS + "logos"

CAUSE_COL_WIDTH = "50px"


def show_circumstances(choice): 
    visible = set_visible(choice)
    add_data_tmp("wounded_dead", 
                    "circumstance_radio", 
                    True)
    button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_circumstances(visible)
    return button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2

def create_circumstances(visible):
    button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause = create_circumstances_buttons(visible)      
    dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_circumstances_dropdown(visible)
    return button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2

def create_circumstances_buttons(visible): 
    with gr.Row() as image_row:
            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_collision = gr.Button("Collision with a means of transport", 
                                             visible=visible,
                                             icon=LOGO_PATH +  '/van.png',
                                             elem_id="buttons-conditions")
                
            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_deliberate_destruction = gr.Button("Destruction / Deliberatly removed", 
                                                          icon=LOGO_PATH +  '/destruction.png',
                                                          visible=visible,
                                                          elem_id="buttons-conditions")
 
            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_indirect_destruction = gr.Button("Indirect destruction", 
                                                        icon=LOGO_PATH +  '/indirect.png',
                                                        visible=visible,
                                                        elem_id="buttons-conditions")

            with gr.Column(scale=1, min_width=CAUSE_COL_WIDTH):
                button_natural_cause = gr.Button("Natural cause", 
                                                 icon=LOGO_PATH +  '/natural.png', 
                                                 visible=visible,
                                                 elem_id="buttons-conditions")
    return button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause

def create_circumstances_dropdown(visible):
    with gr.Row() as dropdown_row:
        dropdown = gr.Dropdown(choices=[], 
                               label="Choices will appear here...",
                               visible=visible, interactive=False, elem_id="dropdown-conditions")
    openfield_level2 = gr.Textbox(visible=False, elem_id="dropdown-conditions")
    dropdown_level2 = gr.Dropdown(choices=[], visible=False, elem_id="dropdown-conditions")
    dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False, elem_id="dropdown-conditions")
    return dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2


     