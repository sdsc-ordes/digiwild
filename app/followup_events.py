import gradio as gr
from config_utils import get_custom_config_dropdowns

def create_followup_section():
    followup_config = get_custom_config_dropdowns("/assets/config/config_followup.json")
    followup_config = followup_config["Event follow-up"]
    gr.Markdown("## Follow-Up Events", label="Title")
    gr.Markdown("Please tell us what you did with the animal.", label="description")
    with gr.Row(): 
        for key, val in followup_config.items():
            followup_label = key
            if "Options" in val.keys(): 
                gr.Dropdown(choices=val["Options"], label=followup_label, visible=True, elem_id="followup")
    with gr.Row(): 
        for key, val in followup_config.items():
            followup_label = key
            if "Open" in val.keys(): 
                gr.Textbox(label=followup_label, visible=True, elem_id="followup")