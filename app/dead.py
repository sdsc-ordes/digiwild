import gradio as gr
from top_section import create_top_section, create_dropdown

def show_section_dead(visible):
    with gr.Column(visible=visible) as section_dead:
        gr.Markdown("# Dead")
        gr.Markdown("Please describe the cause of death")
        
        image_row, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause = create_top_section(visible)      
        dropdown_row, dropdown = create_dropdown(visible)

    return section_dead, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown