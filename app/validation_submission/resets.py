import gradio as gr

from physical.physical_checkbox import process_body_parts

from dotenv import load_dotenv
import os
load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv('PATH_ASSETS')
PATH_ICONS = PATH + PATH_ASSETS + "icons/"

def reset_individual(individual):
    individual = {}
    return individual

def reset_error_box(error_icon, error_box):
    error_icon = gr.Image(PATH_ICONS+"supprimer.png", height=80, width=80, visible=False)
    error_box = gr.Text(value=None, visible=False)
    return error_icon, error_box


def hide_physical(mode):
    (
        checkbox_beak,
        text_beak,
        checkbox_body,
        text_body,
        checkbox_feathers,
        text_feathers,
        checkbox_head,
        text_head,
        checkbox_legs,
        text_legs,
    ) = process_body_parts("wounded", mode, "None")
    return (
        checkbox_beak,
        text_beak,
        checkbox_body,
        text_body,
        checkbox_feathers,
        text_feathers,
        checkbox_head,
        text_head,
        checkbox_legs,
        text_legs,
    )