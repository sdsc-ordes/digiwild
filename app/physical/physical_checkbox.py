import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from utils.utils_checkbox import create_checkbox
from validation_submission.utils_individual import add_data_to_individual


# ---------------------------------------------------------
def get_body_parts():
    """ Get all body parts from the config file 
    Returns:
        list: List of body parts
    """
    dropdown_config = get_custom_config_dropdowns("config_checkbox_physical.json")
    return list(dropdown_config.keys())


def retrieve_config_options(label, dropdown_config):
    """ Retrieve the options for a given label from the config file
    Args:
        label (str): Label to retrieve the options for
        dropdown_config (dict): Config file
    Returns:
        list: List of options
    """
    options = list(dropdown_config[label].keys())
    options = [option.title() for option in options]
    return options


def get_options_description(value, mode):
    """ Get the options and descriptions for a given value
    Args:
        value (str): Value to retrieve the options for
        mode (str): Mode to retrieve the options for
    Returns:
        list: List of options
        list: List of descriptions
    """
    if mode == "simple":
        dropdown_config = get_custom_config_dropdowns(
            "config_checkbox_physical_simple.json"
        )
    elif mode == "advanced":
        dropdown_config = get_custom_config_dropdowns("config_checkbox_physical.json")
    # get options
    options_common = retrieve_config_options("Common", dropdown_config)
    options_for_value = retrieve_config_options(value, dropdown_config)
    options_common.extend(options_for_value)
    options = options_common
    # get descriptions
    descriptions = []
    for key, sub_dict in dropdown_config.items():
        if key == value or key == "Common":
            for _, option_dict in sub_dict.items():
                for description_tag, description in option_dict.items():
                    if "Description" == description_tag:
                        descriptions.append(description)
    return options, descriptions


# ---------------------------------------------------------
def create_checkbox_beak(section, mode, label_checkbox, visible):
    """ Create the checkbox for the beak
    Args:
        section (str): Section of the checkbox
        mode (str): Mode of the checkbox
        label_checkbox (str): Label of the checkbox
        visible (bool): Visibility of the checkbox
    Returns:
        gr.checkbox: Checkboxes for the beak
        gr.text: Text for the beak
    """
    body_part = "Beak"
    options, descriptions = get_options_description(body_part, mode)
    return create_checkbox(
        body_part, section, label_checkbox, visible, options, descriptions
    )


def create_checkbox_body(section, mode, label_checkbox, visible):
    """ Create the checkbox for the body
    Args:
        section (str): Section of the checkbox
        mode (str): Mode of the checkbox
        label_checkbox (str): Label of the checkbox
        visible (bool): Visibility of the checkbox
    Returns:
        gr.checkbox: Checkboxes for the body
        gr.text: Text for the body
    """
    body_part = "Body"
    options, descriptions = get_options_description(body_part, mode)
    return create_checkbox(
        body_part, section, label_checkbox, visible, options, descriptions
    )


def create_checkbox_feathers(section, mode, label_checkbox, visible):
    """ Create the checkbox for the feathers
    Args:
        section (str): Section of the checkbox
        mode (str): Mode of the checkbox
        label_checkbox (str): Label of the checkbox
        visible (bool): Visibility of the checkbox
    Returns:
        gr.checkbox: Checkboxes for the feathers
        gr.text: Text for the feathers
    """
    body_part = "Feathers/Wings/Tail"
    options, descriptions = get_options_description(body_part, mode)
    return create_checkbox(
        body_part, section, label_checkbox, visible, options, descriptions
    )


def create_checkbox_head(section, mode, label_checkbox, visible):
    """ Create the checkbox for the head
    Args:
        section (str): Section of the checkbox
        mode (str): Mode of the checkbox
        label_checkbox (str): Label of the checkbox
        visible (bool): Visibility of the checkbox
    Returns:
        gr.checkbox: Checkboxes for the head
        gr.text: Text for the head
    """
    body_part = "Head incl. eyes"
    options, descriptions = get_options_description(body_part, mode)
    return create_checkbox(
        body_part, section, label_checkbox, visible, options, descriptions
    )


def create_checkbox_legs(section, mode, label_checkbox, visible):
    """ Create the checkbox for the legs
    Args:
        section (str): Section of the checkbox
        mode (str): Mode of the checkbox
        label_checkbox (str): Label of the checkbox
        visible (bool): Visibility of the checkbox
    Returns:
        gr.checkbox: Checkboxes for the legs
        gr.text: Text for the legs
    """
    body_part = "Legs"
    options, descriptions = get_options_description(body_part, mode)
    return create_checkbox(
        body_part, section, label_checkbox, visible, options, descriptions
    )


# ---------------------------------------------------------
def process_body_parts(section, mode, matched_box):
    """ Process the body parts
    Args:
        section (str): Section of the checkbox
        mode (str): Mode of the checkbox
        matched_box (str): Matched box
    Returns:
        gr.checkbox: Checkboxes for the beak
        gr.text: Text for the beak
        gr.checkbox: Checkboxes for the body
        gr.text: Text for the body
        gr.checkbox: Checkboxes for the feathers
        gr.text: Text for the feathers
        gr.checkbox: Checkboxes for the head
        gr.text: Text for the head
        gr.checkbox: Checkboxes for the legs
        gr.text: Text for the legs
    """
    # take all except "Common"
    body_parts = get_body_parts()
    body_parts = body_parts[1:]
    label_checkbox = "Physical changes to "
    visibles = [True if matched_box == body_part else False for body_part in body_parts]
    checkbox_beak, text_beak = create_checkbox_beak(
        section, mode, label_checkbox, visibles[0]
    )
    checkbox_body, text_body = create_checkbox_body(
        section, mode, label_checkbox, visibles[1]
    )
    checkbox_feathers, text_feathers = create_checkbox_feathers(
        section, mode, label_checkbox, visibles[2]
    )
    checkbox_head, text_head = create_checkbox_head(
        section, mode, label_checkbox, visibles[3]
    )
    checkbox_legs, text_legs = create_checkbox_legs(
        section, mode, label_checkbox, visibles[4]
    )
    return (
        checkbox_beak,
        text_beak,
        checkbox_body,
        text_body,
        checkbox_feathers,
        text_feathers,
        checkbox_head,
        text_head,
        checkbox_legs,
        text_legs,
    )


# ---------------------------------------------------------


def on_select_body_part(body_part_checkbox, body_part, individual):
    """ Add the selected body parts to the individual
    Args:
        body_part_checkbox (list): List of selected body parts
        body_part (str): Body part
        individual (dict): Individual
    Returns:
        dict: Individual with the selected body parts
    """
    individual = add_data_to_individual(
        "physical_type_" + body_part.lower(), body_part.lower(), individual
    )
    body_part_checkbox = [
        body_part_check.lower() for body_part_check in body_part_checkbox
    ]
    individual = add_data_to_individual(
        "physical_anomaly_" + body_part.lower(), body_part_checkbox, individual
    )
    return individual
