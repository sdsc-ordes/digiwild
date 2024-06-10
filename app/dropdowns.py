import gradio as gr
import json
import os

def load_config(file_path):
    with open(file_path) as f:
        config = json.load(f)
    return config

def retrieve_config_options(label):
    path = os.getcwd()
    dropdown_config_path = path + "/assets/dropdowns/dropdown_config.json"
    dropdown_config = load_config(dropdown_config_path)
    options = list(dropdown_config[label].keys())
    options = [option.title() for option in options]
    return options


def dropdown_collision():
    label = "Collision with a means of transport"
    options = retrieve_config_options(label)
    return gr.Dropdown(choices=options, label=label, interactive=True)

def dropdown_deliberate_destruction():
    label = "Destruction / Deliberatly removed"
    options = retrieve_config_options(label)
    return gr.Dropdown(choices=options, label=label, interactive=True)        

def dropdown_indirect_destruction(): 
    label = "Indirect destruction"
    options = retrieve_config_options(label)
    return gr.Dropdown(choices=options, label=label, interactive=True)  

def dropdown_natural_cause(): 
    label = "Natural cause"
    options = retrieve_config_options(label)
    return gr.Dropdown(choices=options, label=label, interactive=True)            
