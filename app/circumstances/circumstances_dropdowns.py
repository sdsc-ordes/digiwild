import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from validation_submission.add_json import add_data_tmp

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
    dropdown_config = get_custom_config_dropdowns("config_dropdown_circumstances.json")
    options = retrieve_config_options(label, dropdown_config)
    dropdown = gr.Dropdown(choices=options, label=label, interactive=True, visible=True)
    dropdown_level2, openfield_level2, dropdown_extra_level2 = reinitialise_level2()
    return dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2
    
def dropdown_collision(session_id):
    label = "Collision with a means of transport"
    add_data_tmp(session_id, "wounded_dead", "circumstance", label.lower())
    return create_dropdown_level1(label)

def dropdown_deliberate_destruction(session_id):
    label = "Destruction / Deliberatly removed"
    add_data_tmp(session_id, "wounded_dead", "circumstance", label.lower())
    return create_dropdown_level1(label)     

def dropdown_indirect_destruction(session_id): 
    label = "Indirect destruction"
    add_data_tmp(session_id, "wounded_dead", "circumstance", label.lower())
    return create_dropdown_level1(label) 

def dropdown_natural_cause(session_id): 
    label = "Natural cause"
    add_data_tmp(session_id, "wounded_dead", "circumstance", label.lower())
    return create_dropdown_level1(label)         


#--------------------------------------------------------- LEVEL 2 DROPDOWNS
def get_options(value):
        value = value.lower()
        options_label = None
        options_dropdown= None
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

       
def on_select(session_id, evt: gr.SelectData):  # SelectData is a subclass of EventData
    options_label, options_dropdown, open_field, extras, extras_label = get_options(evt.value)
    add_data_tmp("wounded_dead", 
                    "circumstance_type", 
                    {"type": (evt.value).lower(),
                     "option_dropdown_label" : options_label.lower() if options_label is not None else 'NA',
                     "open_field_label" : open_field.lower() if open_field is not None else 'NA',
                     "extra_label": extras_label.lower() if extras_label is not None else 'NA'
                    })
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

def on_select_dropdown_level2(session_id, evt: gr.SelectData): 
    add_data_tmp(session_id, "wounded_dead", 
                "circumstance_option_dropdown", 
                evt.value.lower())

def on_select_dropdown_extra_level2(session_id, evt: gr.SelectData):  
    add_data_tmp(session_id, "wounded_dead", 
                 "circumstance_extra", 
                 evt.value.lower())
    
def on_change_openfield_level2(session_id, openfield_level2_dead): 
    print("Saving open field")
    add_data_tmp(session_id, "wounded_dead", 
                "circumstance_open_field", 
                str(openfield_level2_dead).lower())