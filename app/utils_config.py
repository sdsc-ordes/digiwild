import json
import os

def load_config(file_path):
    with open(file_path) as f:
        config = json.load(f)
    return config

def get_custom_config_dropdowns(config_path):
    path = os.getcwd()
    dropdown_config_path = path + config_path
    dropdown_config = load_config(dropdown_config_path)
    return dropdown_config

