import gradio as gr

#---------------------------------------------------------
def create_checkbox(value, section, label_checkbox, visible, options, descriptions):
    descriptions_info = "".join([f"\t{option}: {description}\n" for option, description in zip(options, descriptions)])
    checkbox = gr.CheckboxGroup(options, 
                        label=label_checkbox + f" {value}:",
                        visible=visible,
                        interactive=True,
                        elem_id=section)
    text = gr.Textbox(descriptions_info, 
                    label = "Info", 
                    visible=visible,
                    interactive=False,
                    lines=13, 
                    max_lines=15, 
                    elem_id=section)
    return checkbox, text