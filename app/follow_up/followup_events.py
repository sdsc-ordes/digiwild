import gradio as gr
from utils.utils_config import get_custom_config_dropdowns
from utils.utils_json import add_data_to_individual

def create_followup_dropdowns(visible, elem_id): 
    followup_config = get_custom_config_dropdowns("config_followup.json")
    followup_config = followup_config["Event follow-up"]
    fe_collection_dropdown = create_fe_collection_dropdown(followup_config, visible, elem_id)
    fe_recipient_dropdown = create_fe_recipient_dropdown(followup_config, visible, elem_id)
    fe_radio_dropdown = create_fe_radio_dropdown(followup_config, visible, elem_id)
    fe_answer_dropdown = create_fe_answer_dropdown(followup_config, visible, elem_id)
    return fe_collection_dropdown, fe_recipient_dropdown, fe_radio_dropdown, fe_answer_dropdown

def create_followup_open(visible, elem_id): 
    fe_name_recipient = gr.Textbox(label="Name of recipient / museum", visible=visible, 
                                   elem_id=elem_id, interactive=True)
    fe_collection_ref = gr.Textbox(label="Collection reference", visible=visible, 
                                   elem_id=elem_id, interactive=True)
    return fe_name_recipient, fe_collection_ref


def create_fe_collection_dropdown(followup_config, visible, elem_id):
    fe_collection_dropdown = gr.Dropdown(choices=followup_config["Animal collected"]["Options"], label="Animal collected", 
                                         visible=visible, elem_id=elem_id, interactive=True)
    return fe_collection_dropdown

def create_fe_recipient_dropdown(followup_config, visible, elem_id):
    fe_recipient_dropdown = gr.Dropdown(choices=followup_config["Recipient"]["Options"], label="Recipient", 
                                        visible=visible, elem_id=elem_id, interactive=True)
    return fe_recipient_dropdown

def create_fe_radio_dropdown(followup_config, visible, elem_id): 
    fe_radio_dropdown = gr.Dropdown(choices=followup_config["Radiography"]["Options"], label="Radiography", 
                                        visible=visible, elem_id=elem_id, interactive=True)
    return fe_radio_dropdown

def create_fe_answer_dropdown(followup_config, visible, elem_id): 
    fe_answer_dropdown = gr.Dropdown(choices=followup_config["Given answer"]["Options"], label="Given answer", 
                                        visible=visible, elem_id=elem_id, interactive=True)
    return fe_answer_dropdown

def save_fe(value, key): 
    add_data_to_individual(key, value)


    