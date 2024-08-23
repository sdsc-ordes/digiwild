import gradio as gr
from utils_config import get_custom_config_dropdowns
from circumstances_dropdowns import retrieve_config_options

#--------------------------------------------------------- 
def get_body_parts():
    dropdown_config = get_custom_config_dropdowns("/assets/config/config_checkbox_physical.json")
    return list(dropdown_config.keys())

#--------------------------------------------------------- 
def get_options_description(value):
        dropdown_config = get_custom_config_dropdowns("/assets/config/config_checkbox_physical.json")
        # get options
        options = retrieve_config_options("Common", dropdown_config)
        options_for_value = retrieve_config_options(value, dropdown_config)
        options.extend(options_for_value)
        # get descriptions
        descriptions = []
        for key, sub_dict in dropdown_config.items():
            if key==value or key=="Common":
                for _, option_dict in sub_dict.items():
                    for description_tag, description in option_dict.items():
                        if "Description"==description_tag:
                            descriptions.append(description)
        return options, descriptions

#---------------------------------------------------------
def create_checkbox(body_part, section, visible):
    options, descriptions = get_options_description(body_part)
    descriptions_info = "".join([f"\t{option}: {description}\n" for option, description in zip(options, descriptions)])
    checkbox = gr.CheckboxGroup(options, 
                        label=f"Physical changes observed on {body_part}:",
                        visible=visible,
                        interactive=True,
                        elem_id=section)
    text = gr.Textbox(descriptions_info, 
                    label = "Info", 
                    visible=visible,
                    interactive=False,
                    lines=13, 
                    max_lines=15, 
                    elem_id=section)
    return checkbox, text

def create_checkbox_beak(section, visible):
    body_part="Beak"
    return create_checkbox(body_part, section, visible)

def create_checkbox_body(section, visible):
    body_part="Body"
    return create_checkbox(body_part, section, visible)

def create_checkbox_feathers(section, visible):
    body_part="Feathers/Wings/Tail"
    return create_checkbox(body_part, section, visible)

def create_checkbox_head(section, visible):
    body_part="Head incl. eyes"
    return create_checkbox(body_part, section, visible)

def create_checkbox_legs(section, visible):
    body_part="Legs"
    return create_checkbox(body_part, section, visible)

#---------------------------------------------------------
def process_body_parts(section, matched_box):
    #take all except "Common"
    body_parts = get_body_parts()
    body_parts = body_parts[1:]
    visibles = [True if matched_box==body_part else False for body_part in body_parts ]
    checkbox_beak, text_beak = create_checkbox_beak(section, visibles[0])
    checkbox_body, text_body = create_checkbox_body(section, visibles[1])
    checkbox_feathers, text_feathers = create_checkbox_feathers(section, visibles[2])
    checkbox_head, text_head = create_checkbox_head(section, visibles[3])
    checkbox_legs, text_legs = create_checkbox_legs(section, visibles[4])
    return checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
          
     