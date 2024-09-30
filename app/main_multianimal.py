import gradio as gr
from gradio_modal import Modal
import numpy as np

from utils_json import *
from functools import partial
from dead import show_section_dead
from wounded import show_section_wounded
from circumstances import show_causes
from circumstances_dropdowns import *
from physical_select_animal import show_physical, find_bounding_box
from behavior_checkbox import show_behavior
from maps import get_location

     
def save_input(input, df):
    #input_value = str(input)
    df_values = np.array(df) # handle empty dataframe case
    new_row = [input, 0, input]  # default 'age' as 0 for now
    df_values = np.vstack([df_values, new_row])
    df = gr.DataFrame(value=df_values)
    return df

with gr.Blocks() as demo:
    # with gr.Tab("Tab 1"):
    show_btn = gr.Button("Show Modal")
    df = gr.Dataframe(
        headers=["image", "location"],
        #datatype=["str", "number", "str"],
        row_count=1,
        #col_count=(3, "fixed"),
    )
    show_markdown = gr.Markdown("This is a markdown")
    with Modal(visible=False) as modal:
        # ---------------------------------------------------------
        # Intro Text
        with gr.Row():
            with gr.Column(scale=1):
                title = gr.Markdown("# Welcome to Digiwild", label="Title")
                description = gr.Markdown("Please record your wildlife observations here !", label="description")

        # ---------------------------------------------------------
        # Camera
        with gr.Row():
            #with gr.Column(scale=1):
            camera = gr.Image(elem_id="image")
                
        # ---------------------------------------------------------
        # Location
        #with gr.Row():
            with gr.Column(scale=1):
                location = gr.Textbox(visible=True, interactive=True, label="Location of Sighting")
                #display location processing
                identified_location= gr.Textbox(visible=False, interactive=False, 
                                                label="Identified GPS Location")
                with gr.Row():
                    #to clear it
                    clear_location = gr.ClearButton(components=[location], visible=True, interactive=True, scale=1
                                                    )
                    clear_location.click()
                    #to submit it
                    submit_location = gr.Button("Get GPS Coordinates", visible=True, interactive=True, scale=3)
                    submit_location.click(get_location, inputs=[location], outputs=[identified_location])
        
        # ---------------------------------------------------------
         # ---------------------------------------------------------
        # Dead and Wounded Buttons
        gr.Markdown("## The State of the Animal", label="Title")
        gr.Markdown("Please tell us if the animal was wounded or dead.", label="description")
        with gr.Row() as block_form:
            with gr.Column(scale=1):
                butt_wounded = gr.Button("Wounded", elem_id="wounded")
            with gr.Column(scale=1):
                butt_dead = gr.Button("Dead", elem_id="dead")

        # ---------------------------------------------------------
        # Initiate sections
        section_dead, \
            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, \
                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead \
                    = show_section_dead(False)
        section_wounded, radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded, \
            button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
                    behavior_checkbox, behavior_text, \
                        physical_boxes_wounded, \
                            checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs \
                            = show_section_wounded(False)
    
        # ---------------------------------------------------------
        # ---------------------------------------------------------
            # ---------------------------------------------------------
        # Dead Button Logic
        partial_show_section_dead = partial(show_section_dead, True)
        partial_hide_section_wounded = partial(show_section_wounded, False)
        butt_dead.click(partial_show_section_dead, 
                        inputs=None, 
                        outputs=[section_dead, 
                                button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead
                                ])
        butt_dead.click(partial_hide_section_wounded, 
                        inputs=None, 
                        outputs=[section_wounded, 
                                radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded,
                                button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                                behavior_checkbox, behavior_text, 
                                physical_boxes_wounded, 
                                checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
                                ])
        # ---------------------------------------------------------
        # Wounded Button Logic
        partial_show_section_wounded = partial(show_section_wounded, True)
        partial_hide_section_dead = partial(show_section_dead, False)

        butt_wounded.click(partial_show_section_wounded, 
                        inputs=None, 
                        outputs=[section_wounded, 
                                    radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded,
                                    button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                    dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                                    behavior_checkbox, behavior_text, 
                                    physical_boxes_wounded, 
                                    checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
                                    ])
        butt_wounded.click(partial_hide_section_dead, inputs=None, outputs=[section_dead, 
                                                                            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                                                            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead
                                                                            ])
        # ---------------------------------------------------------
        # Dropdowns Dead
        button_collision_dead.click(dropdown_collision,  
                                    outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        button_deliberate_destruction_dead.click(dropdown_deliberate_destruction, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        button_indirect_destruction_dead.click(dropdown_indirect_destruction, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        button_natural_cause_dead.click(dropdown_natural_cause, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])

        dropdown_dead.select(on_select, None, [dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])

        # ---------------------------------------------------------
        # Radio Cause Wounded
        radio_cause_wounded.change(fn=show_causes,
                                inputs=[radio_cause_wounded],
                                outputs=[button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                            dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded]
                                )
        
        # Dropdowns Cause Wounded
        button_collision_wounded.click(dropdown_collision,  
                                    outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        button_deliberate_destruction_wounded.click(dropdown_deliberate_destruction, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        button_indirect_destruction_wounded.click(dropdown_indirect_destruction, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        button_natural_cause_wounded.click(dropdown_natural_cause, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        
        dropdown_wounded.select(on_select, None, [dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])

        # ---------------------------------------------------------
        # Radio Behavior Wounded
        radio_behavior_wounded.change(fn=show_behavior,
                                    inputs=[radio_behavior_wounded, gr.Text("wounded", visible=False)],
                                    outputs=[behavior_checkbox, behavior_text])

        # ---------------------------------------------------------
        # Radio Physical Wounded
        radio_physical_wounded.change(fn=show_physical,
                                    inputs=[radio_physical_wounded, gr.Text("wounded", visible=False)],
                                    outputs=[physical_boxes_wounded])

        # Checkbox Physical Wounded
        physical_boxes_wounded.select(find_bounding_box, 
                        inputs=[physical_boxes_wounded, gr.Textbox(value="wounded", visible=False)], 
                        outputs=[checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
                                    ])
        

        button = gr.Button("Click me")
        # button.click(save_input, 
        #                 inputs=[df],
        #                 outputs=[df])
        button.click(lambda: Modal(visible=False), None, modal)
    show_btn.click(lambda: Modal(visible=True), None, modal)
    show_btn.click(create_json)


     
     
     
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3333)