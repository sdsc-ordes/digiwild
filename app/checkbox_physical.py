import gradio as gr
from config_utils import get_custom_config_dropdowns
from dropdowns_conditions import retrieve_config_options


#--------------------------------------------------------- 
def get_options_description(value):
        dropdown_config = get_custom_config_dropdowns("/assets/config/config_checkbox_physical.json")
        # get options
        options = retrieve_config_options("Common", dropdown_config)
        options_for_value = retrieve_config_options(value, dropdown_config)
        options.extend(options_for_value)
        # get descriptions
        descriptions = []
        for key, sub_dict in dropdown_config.items():
            if key==value or key=="Common":
                for _, option_dict in sub_dict.items():
                    for description_tag, description in option_dict.items():
                        if "Description"==description_tag:
                            descriptions.append(description)
        return options, descriptions
#---------------------------------------------------------
def checkbox(body_part, section):
    options, descriptions = get_options_description(body_part)
    descriptions_info = "".join([f"\t{option}: {description}\n" for option, description in zip(options, descriptions)])
    checkbox = gr.CheckboxGroup(options, 
                     label=f"Physical changes observed on {body_part}:",
                     visible=True,
                     interactive=True,
                     elem_id=section)
    text = gr.Textbox(descriptions_info, 
               label = "Info", 
               interactive=False,
               visible=True,
               elem_id=section)
    return checkbox, text