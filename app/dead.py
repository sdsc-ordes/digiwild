import gradio as gr
from causes import create_causes
from followup_events import create_followup_section


def show_section_dead(visible):
    with gr.Column(visible=visible, elem_id="dead") as section_dead:
        gr.Markdown("# Dead Animal")
        gr.Markdown("## Please describe the cause of death", label="description")
        
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_causes(visible)      
        
        create_followup_section()

    return section_dead, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2
