import gradio as gr
from circumstances import create_causes
from followup_events import create_followup_section
from utils_json import add_data_to_individual  

def show_section_dead(visible):
    if visible==True: 
        add_data_to_individual("dead", "True")
        add_data_to_individual("wounded", "False")
        
    with gr.Column(visible=visible, elem_id="dead") as section_dead:
        gr.Markdown("# Dead Animal")
        gr.Markdown("## Please describe the cause of death", label="description")
        
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_causes(visible)      
        
        create_followup_section()

    return section_dead, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2
