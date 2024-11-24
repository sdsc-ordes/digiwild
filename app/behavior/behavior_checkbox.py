import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from utils.utils_checkbox import create_checkbox
from utils.utils_visible import set_visible
from validation_submission.add_json import add_data_tmp

def on_select_behavior(session_id, behavior_checkbox): 
    behavior_checkbox = [behavior.lower() for behavior in behavior_checkbox]
    add_data_tmp(session_id, "wounded_dead", "behaviors_type", behavior_checkbox)

def retrieve_behavior_options_description():
    dropdown_config = get_custom_config_dropdowns("config_checkbox_behavior.json")
    options = list(dropdown_config.keys())
    options = [option.title() for option in options]
    descriptions =[]
    for _,subdict in dropdown_config.items():
        descriptions.append(subdict["Description"])
    return options, descriptions

def create_behavior_checkbox(section: str, visible):
    options, descriptions = retrieve_behavior_options_description()
    label_checkbox = "Behavior changes observed"
    checkbox, text = create_checkbox("", section, label_checkbox, visible, options, descriptions)
    return checkbox, text

def show_behavior(session_id, choice, section: str): 
    visible = set_visible(choice)
    checkbox, text = create_behavior_checkbox(section, visible)
    add_data_tmp(session_id, "wounded_dead", "behaviors_radio", choice)
    return checkbox, text