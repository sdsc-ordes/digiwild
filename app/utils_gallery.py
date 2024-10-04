import gradio as gr
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from utils_config import load_config
from utils_json import get_json_one_individual, save_to_all_individuals
import os
load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv('PATH_ASSETS')
PATH_CONFIG = PATH + PATH_ASSETS + "config/"

def get_headers(): 
    headers_config = load_config(PATH_CONFIG + "config_headers.json")
    headers = headers_config["headers"]
    return headers

def get_fields(): 
    fields_config = load_config(PATH_CONFIG + "config_fields.json")
    fields = fields_config["fields"]
    return fields

def match_data_to_fields(fields, one_individual): 
    new_row = {}
    for key in fields:
        if key in one_individual:
            if key=="image": 
                new_row[key] = one_individual[key]
            elif type(one_individual[key])==list:
                new_row[key] = ' , '.join(one_individual[key])
            else:
                new_row[key] = one_individual[key]
        else:
            new_row[key] = "NA"
    return new_row



def process_animals(all_animals): 
    processed_animals = []
    for _, animal in all_animals.items(): 
        image = np.array(animal["image"])
        caption = []
        for key, val in animal.items(): 
            if key!="image": 
                if key=="latitude": 
                    caption.extend([
                        " | Latitude: " + str(animal["latitude"])])
                elif key=="longitude": 
                    caption.extend([
                        " | Longitude: " + str(animal["longitude"])])
                elif key=="wounded" and val=="True": 
                    caption.extend([" | Wounded: " + animal["wounded"]])
                elif key=="dead" and val=="True":
                    caption.extend([" | Dead: " + animal["dead"]])
                # elif key=="circumstance": 
                #     caption.extend([" | Circumstances: " , 
                #                     animal["circumstance"],
                #                     animal["circumstance_dropdown_level1"], 
                #                     animal["circumstance_dropdown_level2"],
                #                     animal["circumstance_openfield_level2"], 
                #                     animal["circumstance_dropdown_extra_level2"]])
                # elif key=="behavior": 
                #     caption.extend([" | Behavior: ", animal[key]])
                # elif "physical_changes" in key:
                #     if not(" | Physical Changes: " in caption) :
                #         caption.extend([" | Physical Changes: ",
                #                         "Beak: " + animal["physical_changes_beak"],
                #                         "Body: " + animal["physical_changes_body"], 
                #                         "Head: " + animal["physical_changes_head"],
                #                         "Feathers: " + animal["physical_changes_feathers"], 
                #                         "Legs: " + animal["physical_changes_legs"]])
        caption_str = " ".join(caption)
        animal = (image, caption_str)
        processed_animals.append(animal)
    return processed_animals

def set_gallery_size(len_animals): 
    if len_animals < 10: 
        num_cols=5
        num_rows=2
    else: 
        num_cols = len_animals/2
        num_rows = len_animals/(num_cols)
    return num_cols, num_rows

def save_individual_to_gallery(gallery):
    one_individual = get_json_one_individual()
    fields = get_fields()
    one_individual_matched = match_data_to_fields(fields, one_individual)
    all_animals = save_to_all_individuals(one_individual_matched)
    num_cols, num_rows = set_gallery_size(len(all_animals))
    processed_animals = process_animals(all_animals)
    gallery = gr.Gallery(
        label="Gallery of Records", elem_id="gallery", 
        columns=[num_cols], rows=[num_rows],
        value=processed_animals,
        object_fit="contain", height="auto", interactive=False)
    return gallery
    
# def save_individual_to_df(df): 
#     fields = get_fields()
#     one_individual = get_json_one_individual()
#     headers = get_headers()
#     new_row = match_data_to_fields(fields, one_individual)
#     new_row = format_row(new_row, headers)
#     new_row_df = pd.DataFrame([new_row], columns=headers)  
#     df_new = pd.concat([df, new_row_df], ignore_index=True)
#     df_gr = gr.DataFrame(visible=True,
#                          value=df_new,
#                          headers=headers)
#     return df_gr

# def save_and_rest_df(df):
#     save_all_animals(df)
#     df = gr.Dataframe(fields=get_fields(),
#                       visible=False)
#     return df

# def format_row(new_row, headers):
#     formatted_row = {}
#     #formatted_row["image"] = new_row["image"]
#     for header in headers: 
#         if header=="location": 
#             formatted_row[header] = " | ".join(["Latitude: " + str(new_row["latitude"]), 
#                                                 "Longitude: " + str(new_row["longitude"])])
#         elif header=="state": 
#             formatted_row[header] = " | ".join(["Wounded: " + new_row["wounded"], 
#                                                 "Dead: " + new_row["dead"]])
#         elif header=="circumstance": 
#             formatted_row[header] = " | ".join([new_row["circumstance"],
#                                                 new_row["circumstance_dropdown_level1"], 
#                                                 new_row["circumstance_dropdown_level2"],
#                                                 new_row["circumstance_openfield_level2"], 
#                                                 new_row["circumstance_dropdown_extra_level2"]])
#         elif header=="behavior": 
#             formatted_row[header] = new_row[header]
#         elif header=="physical_changes":
#             formatted_row[header] = " | ".join([new_row["physical_changes_beak"],
#                                                 new_row["physical_changes_body"], 
#                                                 new_row["physical_changes_head"],
#                                                 new_row["physical_changes_feathers"], 
#                                                 new_row["physical_changes_legs"]])
#     return list(formatted_row.values())
