import gradio as gr
from config_utils import get_custom_config_dropdowns


#--------------------------------------------------------- LEVEL 1 DROPDOWNS
def retrieve_config_options(label, dropdown_config):
    options = list(dropdown_config[label].keys())
    options = [option.title() for option in options]
    return options

def reinitialise_level2(): 
    dropdown_level2 = gr.Dropdown(choices=[], visible=False)
    openfield_level2 = gr.Textbox(visible=False)
    dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False)
    return dropdown_level2, openfield_level2, dropdown_extra_level2

def create_dropdown_level1(label): 
    dropdown_config = get_custom_config_dropdowns("/assets/config/config_dropdown_conditions.json")
    options = retrieve_config_options(label, dropdown_config)
    dropdown = gr.Dropdown(choices=options, label=label, interactive=True, visible=True)
    dropdown_level2, openfield_level2, dropdown_extra_level2 = reinitialise_level2()
    return dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2
    
def dropdown_collision():
    label = "Collision with a means of transport"
    return create_dropdown_level1(label)

def dropdown_deliberate_destruction():
    label = "Destruction / Deliberatly removed"
    return create_dropdown_level1(label)     

def dropdown_indirect_destruction(): 
    label = "Indirect destruction"
    return create_dropdown_level1(label) 

def dropdown_natural_cause(): 
    label = "Natural cause"
    return create_dropdown_level1(label)         


#--------------------------------------------------------- LEVEL 2 DROPDOWNS
def get_options(value):
        value = value.lower()
        options_dropdown= None
        open_field = None
        extras = None
        extras_label = None
        dropdown_config = get_custom_config_dropdowns("/assets/config/config_dropdown_conditions.json")
        for _, sub_dict in dropdown_config.items():
            nested_dict = sub_dict.get(value)
            if nested_dict is not None: 
                if "Options" in nested_dict.keys():
                    options_dropdown = nested_dict["Options"]
                    options_dropdown = [option.title() for option in options_dropdown]
                if "Open" in nested_dict.keys():
                    open_field = nested_dict["Open"]
                    open_field = open_field.title()
                if "Extra" in nested_dict.keys():
                    for key, val in nested_dict["Extra"].items():
                        extras_label = key
                        extras = val
                        extras = [extra.title() for extra in extras]
        return options_dropdown, open_field, extras, extras_label
            
def on_select(evt: gr.SelectData):  # SelectData is a subclass of EventData
    options_dropdown, open_field, extras, extras_label = get_options(evt.value)
    if options_dropdown is not None:
        dropdown_level2 = gr.Dropdown(choices=options_dropdown, label=evt.value, interactive=True, visible=True)
    else: 
        dropdown_level2 = gr.Dropdown(choices=[], visible=False)

    if open_field is not None:
        openfield_level2 = gr.Textbox(label=open_field, interactive=True, visible=True)
    else: 
        openfield_level2 = gr.Textbox(visible=False)

    if extras is not None: 
        dropdown_extra_level2 = gr.Dropdown(choices=extras, label=extras_label, interactive=True, visible=True)
    else: 
        dropdown_extra_level2 = gr.Dropdown(choices=[], visible=False)
    return dropdown_level2, openfield_level2, dropdown_extra_level2