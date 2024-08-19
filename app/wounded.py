import gradio as gr
from causes import create_causes
from followup_events import create_followup_section

def show_section_wounded(visible):
    with gr.Column(visible=visible, elem_id="wounded") as wounded_section:
        gr.Markdown("# Wounded Animal")
        
        gr.Markdown("## Do you know what conditions caused this?", label="description")
        radio_cause = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2 = create_causes(visible=False)

        gr.Markdown("## Is the bird displaying behavioural changes?" , label="description")
        radio_behaviour = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)

        gr.Markdown("## Are there physical changes on the bird?" , label="description")
        radio_physical = gr.Radio(["Yes", "No"], value=None, show_label=False, interactive=True)
        create_followup_section()

    # Change variables and names
    return wounded_section, radio_cause, radio_behaviour, radio_physical, button_collision, button_deliberate_destruction, button_indirect_destruction, button_natural_cause, dropdown, dropdown_level2, openfield_level2, dropdown_extra_level2
