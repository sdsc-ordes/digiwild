import gradio as gr
from circumstances.circumstances import create_circumstances
from physical.physical_select_animal import create_bird_anatomy
from physical.physical_checkbox import process_body_parts
from follow_up.followup_events import create_followup_dropdowns, create_followup_open
from validation_submission.add_json import add_data_to_individual

def show_section_dead(visible, individual):
    if visible==True: 
        individual = add_data_to_individual("wounded_state", "No", individual)
        individual = add_data_to_individual("dead_state", "Yes", individual)
        
    with gr.Column(visible=visible, elem_id="dead") as section_dead:
        gr.Markdown("# Dead Animal")
        
        gr.Markdown("## Do you know what conditions caused this?", label="description")
        radio_cause = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_circumstances(visible=False)      
        
        gr.Markdown("## Are there physical changes on the bird?" , label="description")
        radio_physical = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        with gr.Row():
            physical_boxes = create_bird_anatomy(False, "dead")
            with gr.Column():
                checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs = process_body_parts("dead", "None")

        gr.Markdown("## Follow-Up Events", label="Title")
        gr.Markdown("Please tell us what you did with the animal.", label="description")
        with gr.Row(): 
            fe_collection_dropdown, fe_recepient_dropdown, fe_radio_dropdown, fe_answer_dropdown = create_followup_dropdowns(visible, "dead")
        with gr.Row(): 
            fe_name_recipient, fe_collection_ref = create_followup_open(visible, "dead")


    return section_dead, individual, radio_cause, radio_physical,\
         button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, \
          dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2, \
          physical_boxes, \
          checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs, \
          fe_collection_dropdown, fe_recepient_dropdown, fe_radio_dropdown, fe_answer_dropdown, fe_name_recipient, fe_collection_ref
