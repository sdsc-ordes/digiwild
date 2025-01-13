import gradio as gr
import pandas as pd
from gradio_modal import Modal
from PIL import Image
from io import BytesIO
import base64

from validation_submission.submission import validate_save_individual
from validation_submission.get_json import get_json_all_individuals

HEADERS = ["Identifier", "Location", "Wounded", "Dead"]


def save_display_individual(gallery, df, error_box, data):
    individual, error_box, data = validate_save_individual(data, error_box)
    if individual:
        all_animals = get_json_all_individuals()
        gallery_animals = process_animals_for_gallery(all_animals)
        gallery = make_gallery(gallery_animals)
        df_animals = process_animals_for_df(all_animals)
        df = make_df(df_animals)
    return gallery, df, error_box, data

# ---------------------------------- 
# GALLERY 

def convert_image(image_base64_str): 
    im = Image.open(BytesIO(base64.b64decode(image_base64_str)))
    return im

def set_gallery_size(len_animals): 
    if len_animals < 10: 
        num_cols=5
        num_rows=2
    else: 
        num_cols = len_animals/2
        num_rows = len_animals/(num_cols)
    return num_cols, num_rows

def process_animals_for_gallery(all_animals): 
    gallery_animals = []
    for _, animal in all_animals.items(): 
        image = convert_image(animal["image"]["image"])
        caption = animal["identifier"]
        animal = (image, caption)
        gallery_animals.append(animal)
    return gallery_animals

def make_gallery(gallery_animals):
    num_cols, num_rows = set_gallery_size(len(gallery_animals))
    gallery = gr.Gallery(
        label="Gallery of Records", elem_id="gallery", 
        columns=[num_cols], rows=[num_rows],
        value=gallery_animals,
        object_fit="contain", height="auto", interactive=False)
    return gallery

def keep_only_values(dict_to_filter): 
    info_text = ""
    values_to_ignore = ["Yes", "No", "NA"]
    if dict_to_filter:
        for key, val in dict_to_filter.items(): 
            if type(val) is dict: 
                subset_text = keep_only_values(val)
                info_text += f"{subset_text}"
            elif type(val) is list:
                for item in val: 
                    if type(item) is dict: 
                        subset_text = keep_only_values(item)
                        info_text += f"{subset_text}"
            elif (val is not None) and (type(val) is not bool) and (val not in values_to_ignore): 
                info_text += f" {key} : {val} |"
            else:
                print("Ignoring value: ", val)
                print("Associated key: ", key)
    else: 
        info_text = "NaN"
    return info_text

# ---------------------------------- 
# DATAFRAME 

def process_animals_for_df(all_animals):
    df_animals = {}
    identifiers =[]
    geo =[]
    wounded =[]
    dead =[]
    for _, animal in all_animals.items(): 
        identifier_value = animal["identifier"]
        identifiers.append(identifier_value)
        geo_dict = animal["geolocalisation"]
        geo_values = keep_only_values(geo_dict)
        geo.append(geo_values)
        wounded_dict = animal["wounded"]
        wounded_values = keep_only_values(wounded_dict)
        wounded.append(wounded_values)
        dead_dict = animal["dead"]
        dead_values = keep_only_values(dead_dict)
        dead.append(dead_values)
    df_animals["Identifier"] = identifiers
    df_animals["Location"] = geo
    df_animals["Wounded"] = wounded
    df_animals["Dead"] = dead
    return df_animals


def make_df(df_animals):
    df = pd.DataFrame.from_dict(df_animals)
    styled_df = df.style.set_properties(**{
    'min-width': '25px',
    'max-width': '50px',  # Adjust width as needed
    'white-space': 'normal',  # Allows text to wrap to the next line
    'word-wrap': 'break-word'  # Breaks long words to fit within the width
    })
    df_gradio = gr.DataFrame(visible=True,
                         value=styled_df,
                         headers=HEADERS, interactive=False)
    return df_gradio

