import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from utils.utils_checkbox import create_checkbox
from utils.utils_visible import set_visible
from validation_submission.utils_individual import add_data_to_individual


def on_select_behavior(behavior_checkbox, individual):
    """
    This function is called when the user selects a behavior from the checkbox.
    It adds the selected behavior to the individual dictionary.
    Args: 
        behavior_checkbox: list of behaviors selected by the user
        individual: dictionary of individual data
    Returns:
        individual: dictionary of individual data with the selected behavior added
    """
    behavior_checkbox = [behavior.lower() for behavior in behavior_checkbox]
    individual = add_data_to_individual("behaviors_type", behavior_checkbox, individual)
    return individual


def retrieve_behavior_options_description(mode: str):
    """
    This function retrieves the behavior options and their descriptions from the config file.
    Args:
        mode: string indicating the mode of the application (simple or advanced)
    Returns:
        options: list of behavior options
        descriptions: list of behavior descriptions
    """
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
    """
    This function creates the behavior checkbox.
    Args:
        section: string indicating the section of the application
        mode: string indicating the mode of the application (simple or advanced)
        visible: boolean indicating whether the checkbox is visible
    Returns:
        checkbox: gradio checkbox object
        text: gradio text object
    """
    options, descriptions = retrieve_behavior_options_description(mode)
    label_checkbox = "Behavior changes observed"
    checkbox, text = create_checkbox(
        "", section, label_checkbox, visible, options, descriptions
    )
    return checkbox, text


def show_behavior(choice, section: str, mode: str, individual):
    """
    This function shows the behavior checkbox.
    Args:
        choice: string indicating the behavior choice
        section: string indicating the section of the application
        mode: string indicating the mode of the application (simple or advanced)
        individual: dictionary of individual data
    Returns:
        checkbox: gradio checkbox object
        text: gradio text object explaining behavior
        individual: dictionary of individual data with the selected behavior
    """
    # print(f"Show Behavior: {mode}")
    visible = set_visible(choice)
    checkbox, text = create_behavior_checkbox(section, mode, visible)
    individual = add_data_to_individual("behaviors_radio", choice, individual)
    return checkbox, text, individual
