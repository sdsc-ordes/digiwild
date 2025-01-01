import gradio as gr
from dotenv import load_dotenv
import os
from typing import List
from shapely.geometry import Point

from physical.physical_checkbox import *
from physical.physical_boxes_define import gdf
from utils.utils_visible import set_visible

load_dotenv()
PATH_ASSETS = os.getenv('PATH_ASSETS')

# Function to find the matching bounding box for a given point and return the image with boxes
def find_bounding_box(evt: gr.SelectData, img, section: str):
    x, y = evt.index[0], evt.index[1]
    point = Point(x, y)
    match = gdf[gdf.contains(point)]
    if not match.empty:
        matched_box = match.iloc[0]['name']
        checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs = process_body_parts(section, matched_box)
    else:
        matched_box = None
        checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs = process_body_parts(section, matched_box)
    return checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs

    

# Gradio app
def create_bird_anatomy(visible, section: str):
    # Draw bounding boxes on the image
    print
    img_with_boxes = gr.Image(value=PATH_ASSETS+'images/bird_boxed.png', 
                            show_label=False, 
                            height="600px",
                            elem_id=section,
                            visible=visible)
    return img_with_boxes

def show_physical(choice, section: str, individual): 
    visible = set_visible(choice)
    physical_boxes = create_bird_anatomy(visible, section)
    individual = add_data_tmp("wounded_dead", "physical_radio", choice, individual)
    return physical_boxes, individual






