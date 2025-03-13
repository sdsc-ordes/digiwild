import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from validation_submission.utils_individual import add_data_to_individual


# --------------------------------------------------------- LEVEL 1 DROPDOWNS
def retrieve_config_options(label, dropdown_config):
    """ Function retrieves the options for the dropdowns from the config file 
    Args:
        label: string indicating the label of the dropdown
        dropdown_config: dictionary containing the dropdown configuration
    Returns:
        options: list of options for the dropdown
    """
    options = list(dropdown_config[label].keys())
    options = [option.title() for option in options]
    return options

def create_dropdown_level1(label, individual):
    """ Function creates the level 1 dropdowns
    Args:
        label: string indicating the label of the dropdown
        individual: dictionary of individual data
    Returns:
        dropdown: gradio dropdown object
        dropdown_level2: gradio dropdown object
        openfield_level2: gradio text object
        dropdown_extra_level2: gradio dropdown object
        individual: dictionary of individual data
    """
    dropdown_config = get_custom_config_dropdowns("config_dropdown_circumstances.json")
    options = retrieve_config_options(label, dropdown_config)
    dropdown = gr.Dropdown(choices=options, label=label, interactive=True, visible=True)
    dropdown_level2, openfield_level2, dropdown_extra_level2 = reinitialise_level2()
    return (
        dropdown,
        dropdown_level2,
        openfield_level2,
        dropdown_extra_level2,
        individual,
    )


def dropdown_collision(individual):
    """ Function creates the dropdown for the collision with a means of transport
    Args:
        individual: dictionary of individual data
    Returns:
        dropdown: gradio dropdown object
    """
    label = "Collision with a means of transport"
    individual = add_data_to_individual("circumstance", label.lower(), individual)
    return create_dropdown_level1(label, individual)


def dropdown_deliberate_destruction(individual):
    """ Function creates the dropdown for the deliberate destruction
    Args:
        individual: dictionary of individual data
    Returns:
        dropdown: gradio dropdown object
    """
    label = "Destruction / Deliberatly removed"
    individual = add_data_to_individual("circumstance", label.lower(), individual)
    return create_dropdown_level1(label, individual)


def dropdown_indirect_destruction(individual):
    """ Function creates the dropdown for the indirect destruction
    Args:
        individual: dictionary of individual data
    Returns:
        dropdown: gradio dropdown object
    """
    label = "Indirect destruction"
    individual = add_data_to_individual("circumstance", label.lower(), individual)
    return create_dropdown_level1(label, individual)


def dropdown_natural_cause(individual):
    """ Function creates the dropdown for the natural cause
    Args:
        individual: dictionary of individual data
    Returns:
        dropdown: gradio dropdown object
    """
    label = "Natural cause"
    individual = add_data_to_individual("circumstance", label.lower(), individual)
    return create_dropdown_level1(label, individual)


# --------------------------------------------------------- LEVEL 2 DROPDOWNS

def reinitialise_level2():
    """ Function reinitialises the level 2 dropdowns
    Returns:
        dropdown_level2: gradio dropdown object
        openfield_level2: gradio text object
        dropdown_extra_level2: gradio dropdown object
    """
    dropdown_level2 = gr.Dropdown(choices=[], visible=False)
    openfield_level2 = gr.Textbox(visible=False)
    dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False)
    return dropdown_level2, openfield_level2, dropdown_extra_level2

def get_options(value):
    """ Function retrieves the options for the dropdowns
    Args:
        value: string indicating the value of the dropdown
    Returns:
        options_label: string indicating the label of the options dropdown
        options_dropdown: list of options for the options dropdown
        open_field: string indicating the label of the open field
        extras: list of extras for the dropdown
        extras_label: string indicating the label of the extras dropdown
    """
    value = value.lower()
    options_label = None
    options_dropdown = None
    open_field = None
    extras = None
    extras_label = None
    dropdown_config = get_custom_config_dropdowns("config_dropdown_circumstances.json")
    for _, sub_dict in dropdown_config.items():
        nested_dict = sub_dict.get(value)
        if nested_dict is not None:
            if "Options" in nested_dict.keys():
                options_dict = nested_dict["Options"]
                options_label = list(options_dict.keys())[0]
                options_dropdown = list(options_dict.values())[0]
                options_dropdown = [option.title() for option in options_dropdown]
            if "Open" in nested_dict.keys():
                open_field = nested_dict["Open"]
                open_field = open_field.title()
            if "Extra" in nested_dict.keys():
                for key, val in nested_dict["Extra"].items():
                    extras_label = key
                    extras = val
                    extras = [extra.title() for extra in extras]
    return options_label, options_dropdown, open_field, extras, extras_label


def on_select(evt: gr.SelectData, individual):  # SelectData is a subclass of EventData
    """ Function is called when the user selects a value from the dropdown
    Args:
        evt: gr.SelectData object (the object selected by the user)
        individual: dictionary of individual data where the selected value is added
    Returns:
        dropdown_level2: gradio dropdown object
        openfield_level2: gradio text object
        dropdown_extra_level2: gradio dropdown object
        individual: dictionary of individual data
    """
    options_label, options_dropdown, open_field, extras, extras_label = get_options(
        evt.value
    )
    individual = add_data_to_individual(
        "circumstance_type",
        {
            "type": (evt.value).lower(),
            "option_dropdown_label": options_label.lower()
            if options_label is not None
            else "NA",
            "open_field_label": open_field.lower() if open_field is not None else "NA",
            "extra_label": extras_label.lower() if extras_label is not None else "NA",
        },
        individual,
    )
    if options_dropdown is not None:
        dropdown_level2 = gr.Dropdown(
            choices=options_dropdown, label=evt.value, interactive=True, visible=True
        )
    else:
        dropdown_level2 = gr.Dropdown(choices=[], visible=False)

    if open_field is not None:
        openfield_level2 = gr.Textbox(label=open_field, interactive=True, visible=True)
    else:
        openfield_level2 = gr.Textbox(visible=False)

    if extras is not None:
        dropdown_extra_level2 = gr.Dropdown(
            choices=extras, label=extras_label, interactive=True, visible=True
        )
    else:
        dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False)
    return dropdown_level2, openfield_level2, dropdown_extra_level2, individual


def on_select_dropdown_level2(evt: gr.SelectData, individual):
    """ Function is called when the user selects a value from the level 2 dropdown
    Args:
        evt: gr.SelectData object (the object selected by the user)
        individual: dictionary of individual data where the selected value is added
    Returns:
        individual: dictionary of individual data
    """
    individual = add_data_to_individual(
        "circumstance_option_dropdown", evt.value.lower(), individual
    )
    return individual


def on_select_dropdown_extra_level2(evt: gr.SelectData, individual):
    """ Function is called when the user selects a value from the extra level 2 dropdown
    Args:
        evt: gr.SelectData object (the object selected by the user)
        individual: dictionary of individual data where the selected value is added
    Returns:
        individual: dictionary of individual data
    """
    individual = add_data_to_individual(
        "circumstance_extra", evt.value.lower(), individual
    )
    return individual


def on_change_openfield_level2(openfield_level2_dead, individual):
    """ Function is called when the user changes the open field text
    Args:
        openfield_level2_dead: string filled in by the user
        individual: dictionary of individual data where the open field text is added"
    Returns:
        individual: dictionary of individual data
    """
    individual = add_data_to_individual(
        "circumstance_open_field", str(openfield_level2_dead).lower(), individual
    )
    return individual
