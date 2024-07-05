import gradio as gr
from top_section import create_top_section, create_dropdown
from followup_events import create_followup_section


def show_section_dead(visible):
    with gr.Column(visible=visible, elem_id="dead") as section_dead:
        gr.Markdown("# Dead Animal")
        gr.Markdown("## Please describe the cause of death")
        
        image_row, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause = create_top_section(visible)      
        dropdown_row, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_dropdown(visible)
        
        gr.Markdown("## Follow-up Events")
        create_followup_section()

    return section_dead, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2
