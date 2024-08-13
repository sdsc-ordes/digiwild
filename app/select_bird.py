import gradio as gr
# from gradio_image_prompter import ImagePrompter
from typing import List
from shapely.geometry import Point

from boxes_define import gdf

# Function to find the matching bounding box for a given point and return the image with boxes
def find_bounding_box(evt: gr.SelectData, img):
    x, y = evt.index[0], evt.index[1]
    point = Point(x, y)
    match = gdf[gdf.contains(point)]
    if not match.empty:
        matched_box = match.iloc[0]['name']
    else:
        matched_box = "No bounding box found"
    return matched_box

# Gradio app
def create_bird_anatomy():
    # Draw bounding boxes on the image
    img_with_boxes = gr.Image(value='assets/images/bird_boxed.png', 
                              show_label=False, 
                              height="600px")
    matched_box = gr.Textbox(label="Selected box")
    return img_with_boxes, matched_box





