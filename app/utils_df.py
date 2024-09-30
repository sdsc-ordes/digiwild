import gradio as gr
import pandas as pd
from dotenv import load_dotenv
from utils_config import load_config
from utils_json import get_json_one_individual
import os
load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv('PATH_ASSETS')
PATH_CONFIG = PATH + PATH_ASSETS + "config/"

def get_headers(): 
    headers_config = load_config(PATH_CONFIG + "config_df.json")
    headers = headers_config["headers"]
    return headers

def match_data_to_headers(headers, one_individual): 
    new_row = {}
    for key in headers:
        if key in one_individual:
            if type(one_individual[key])==list:
                new_row[key] = ' , '.join(one_individual[key])
            else:
                new_row[key] = one_individual[key]
        else:
            new_row[key] = "NA"
    return list(new_row.values())

def save_individual_to_df(df): 
    headers = get_headers()
    one_individual = get_json_one_individual()
    new_row = match_data_to_headers(headers, one_individual)
    new_row_df = pd.DataFrame([new_row], columns=headers)  
    df_new = pd.concat([df, new_row_df], ignore_index=True)
    df_gr = gr.DataFrame(visible=True,
                         value=df_new,
                         headers=headers)
    return df_gr
