import gradio as gr
from circumstances.circumstances import create_circumstances
from follow_up.followup_events import create_followup_dropdowns, create_followup_open
from validation_submission.add_json import add_data_to_individual  

def show_section_dead(visible):
    if visible==True: 
        add_data_to_individual("dead_bool", "True")
        add_data_to_individual("wounded_bool", "False")
        
    with gr.Column(visible=visible, elem_id="dead") as section_dead:
        gr.Markdown("# Dead Animal")
        gr.Markdown("## Please describe the cause of death", label="description")
        
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_circumstances(visible)      
        
        gr.Markdown("## Follow-Up Events", label="Title")
        gr.Markdown("Please tell us what you did with the animal.", label="description")
        with gr.Row(): 
            fe_collection_dropdown, fe_recepient_dropdown, fe_radio_dropdown, fe_answer_dropdown = create_followup_dropdowns(visible, "dead")
        with gr.Row(): 
            fe_name_recipient, fe_collection_ref = create_followup_open(visible, "dead")


    return section_dead, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, \
          dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2, \
          fe_collection_dropdown, fe_recepient_dropdown, fe_radio_dropdown, fe_answer_dropdown, fe_name_recipient, fe_collection_ref
