import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from utils.utils_checkbox import create_checkbox
from utils.utils_visible import set_visible
from validation_submission.utils_individual import add_data_to_individual


def on_select_behavior(behavior_checkbox, individual):
    behavior_checkbox = [behavior.lower() for behavior in behavior_checkbox]
    individual = add_data_to_individual("behaviors_type", behavior_checkbox, individual)
    return individual


def retrieve_behavior_options_description(mode: str):
    # print(f"Retrieve Behavior Option Description: {mode}")
    if mode == "simple":
        dropdown_config = get_custom_config_dropdowns(
            "config_checkbox_behavior_simple.json"
        )
    elif mode == "advanced":
        dropdown_config = get_custom_config_dropdowns("config_checkbox_behavior.json")
    options = list(dropdown_config.keys())
    options = [option.title() for option in options]
    descriptions = []
    for _, subdict in dropdown_config.items():
        descriptions.append(subdict["Description"])
    return options, descriptions


def create_behavior_checkbox(section: str, mode: str, visible):
    options, descriptions = retrieve_behavior_options_description(mode)
    label_checkbox = "Behavior changes observed"
    checkbox, text = create_checkbox(
        "", section, label_checkbox, visible, options, descriptions
    )
    return checkbox, text


def show_behavior(choice, section: str, mode: str, individual):
    # print(f"Show Behavior: {mode}")
    visible = set_visible(choice)
    checkbox, text = create_behavior_checkbox(section, mode, visible)
    individual = add_data_to_individual("behaviors_radio", choice, individual)
    return checkbox, text, individual
