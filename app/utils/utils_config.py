import json
import os
from dotenv import load_dotenv
import os

load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv("PATH_ASSETS")
PATH_CONFIG = PATH + PATH_ASSETS + "config/"


def load_config(file_path):
    with open(file_path) as f:
        config = json.load(f)
    return config


def get_custom_config_dropdowns(config_path):
    dropdown_config_path = PATH_CONFIG + config_path
    dropdown_config = load_config(dropdown_config_path)
    return dropdown_config
