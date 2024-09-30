import gradio as gr
from circumstances import create_causes
from physical_select_animal import create_bird_anatomy
from physical_checkbox import process_body_parts
from behavior_checkbox import create_behavior_checkbox
from followup_events import create_followup_section
from utils_json import add_data_to_individual  

def show_section_wounded(visible):
    if visible==True: 
        add_data_to_individual("wounded", "True")
    else: 
        add_data_to_individual("wounded", "False")
    with gr.Column(visible=visible, elem_id="wounded") as wounded_section:
        gr.Markdown("# Wounded Animal")
        
        gr.Markdown("## Do you know what conditions caused this?", label="description")
        radio_cause = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_causes(visible=False)

        gr.Markdown("## Is the bird displaying behavioural changes?" , label="description")
        radio_behaviour = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        with gr.Row():
            behavior_checkbox, behavior_text = create_behavior_checkbox("wounded", False)

        gr.Markdown("## Are there physical changes on the bird?" , label="description")
        radio_physical = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        with gr.Row():
            physical_boxes = create_bird_anatomy(False, "wounded")
            with gr.Column():
                checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs = process_body_parts("wounded", "None")


        gr.Markdown("## Follow-Up Events", label="Title")
        create_followup_section()

    # Change variables and names
    return wounded_section, radio_cause, radio_behaviour, radio_physical, \
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, \
        dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2, \
        behavior_checkbox, behavior_text, \
        physical_boxes, \
        checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
