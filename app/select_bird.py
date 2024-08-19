import gradio as gr
# from gradio_image_prompter import ImagePrompter
from typing import List
from shapely.geometry import Point
from checkbox_physical import *

from boxes_define import gdf

# Function to find the matching bounding box for a given point and return the image with boxes
def find_bounding_box(evt: gr.SelectData, img, section: str):
    x, y = evt.index[0], evt.index[1]
    point = Point(x, y)
    match = gdf[gdf.contains(point)]
    if not match.empty:
        matched_box = match.iloc[0]['name']
        physical_checkbox, physical_text = checkbox(matched_box, section)
    else:
        matched_box = "None"
        physical_checkbox, physical_text = create_template_checkbox()
    return physical_checkbox, physical_text

def create_template_checkbox(): 
    #templates
    checkbox = gr.CheckboxGroup([], label="", visible=False)
    text = gr.Textbox("", label = "", interactive=False, visible=False) 
    return checkbox, text

# Gradio app
def create_bird_anatomy(section: str):
    # Draw bounding boxes on the image
    img_with_boxes = gr.Image(value='assets/images/bird_boxed.png', 
                              show_label=False, 
                              height="600px",
                              elem_id=section)
    checkbox, text = create_template_checkbox()
    return img_with_boxes, checkbox, text





