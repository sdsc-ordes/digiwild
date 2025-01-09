import gradio as gr

#---------------------------------------------------------
def create_checkbox(value, section, label_checkbox, visible, options, descriptions):
    descriptions_info = "<br><br>".join([f"* **{option}**: {description}" for option, description in zip(options, descriptions)])
    checkbox = gr.CheckboxGroup(options, 
                        label=label_checkbox + f" {value}:",
                        visible=visible,
                        interactive=True,
                        elem_id=section)
    text = gr.Markdown(descriptions_info, 
                    label = "Info", 
                    visible=visible,
                    #interactive=False,
                    #lines=13, 
                    #max_lines=15, 
                    elem_id=section)
    return checkbox, text