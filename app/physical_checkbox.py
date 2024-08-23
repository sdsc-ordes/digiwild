import gradio as gr
from utils_config import get_custom_config_dropdowns
from utils_checkbox import create_checkbox
#--------------------------------------------------------- 
def get_body_parts():
    dropdown_config = get_custom_config_dropdowns("/assets/config/config_checkbox_physical.json")
    return list(dropdown_config.keys())

def retrieve_config_options(label, dropdown_config):
    options = list(dropdown_config[label].keys())
    options = [option.title() for option in options]
    return options

def get_options_description(value):
        dropdown_config = get_custom_config_dropdowns("/assets/config/config_checkbox_physical.json")
        # get options
        options_common = retrieve_config_options("Common", dropdown_config)
        options_for_value = retrieve_config_options(value, dropdown_config)
        options_common.extend(options_for_value)
        options = options_common
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
def create_checkbox_beak(section, label_checkbox, visible):
    body_part="Beak"
    options, descriptions = get_options_description(body_part)
    return create_checkbox(body_part, section, label_checkbox, visible, options, descriptions)

def create_checkbox_body(section, label_checkbox, visible):
    body_part="Body"
    options, descriptions = get_options_description(body_part)
    return create_checkbox(body_part, section, label_checkbox, visible, options, descriptions)

def create_checkbox_feathers(section, label_checkbox, visible):
    body_part="Feathers/Wings/Tail"
    options, descriptions = get_options_description(body_part)
    return create_checkbox(body_part, section, label_checkbox, visible, options, descriptions)

def create_checkbox_head(section, label_checkbox, visible):
    body_part="Head incl. eyes"
    options, descriptions = get_options_description(body_part)
    return create_checkbox(body_part, section, label_checkbox, visible, options, descriptions)

def create_checkbox_legs(section, label_checkbox, visible):
    body_part="Legs"
    options, descriptions = get_options_description(body_part)
    return create_checkbox(body_part, section, label_checkbox, visible, options, descriptions)

#---------------------------------------------------------
def process_body_parts(section, matched_box):
    #take all except "Common"
    body_parts = get_body_parts()
    body_parts = body_parts[1:]
    label_checkbox = "Physical changes to "
    visibles = [True if matched_box==body_part else False for body_part in body_parts ]
    checkbox_beak, text_beak = create_checkbox_beak(section, label_checkbox, visibles[0])
    checkbox_body, text_body = create_checkbox_body(section, label_checkbox, visibles[1])
    checkbox_feathers, text_feathers = create_checkbox_feathers(section, label_checkbox, visibles[2])
    checkbox_head, text_head = create_checkbox_head(section, label_checkbox, visibles[3])
    checkbox_legs, text_legs = create_checkbox_legs(section, label_checkbox, visibles[4])
    return checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
          
     