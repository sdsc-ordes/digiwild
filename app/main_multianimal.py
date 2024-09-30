import gradio as gr
from gradio_modal import Modal

from utils_df import get_headers
from utils_json import *
from utils_df import save_individual_to_df, get_headers
from maps import get_location
from functools import partial
from dead import show_section_dead
from wounded import show_section_wounded
from circumstances import show_causes
from circumstances_dropdowns import *
from physical_select_animal import show_physical, find_bounding_box
from physical_checkbox import on_select_body_part
from behavior_checkbox import show_behavior, on_select_behavior
from style import *
from theme import theme, css

with gr.Blocks(theme=theme, css=css) as demo:
    # with gr.Tab("Tab 1"):
    show_modal = gr.Button("Add an Animal")
    df = gr.Dataframe(headers=get_headers(),
                      visible=False)
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
                    #to submit it
                    submit_location = gr.Button("Get GPS Coordinates", 
                                                visible=True, interactive=True, scale=3)
                    submit_location.click(get_location, inputs=[location], outputs=[identified_location])
                    #to clear it
                    clear_location = gr.ClearButton(components=[location, identified_location], 
                                                    visible=True, interactive=True, scale=1
                                                    )
                    clear_location.click()
        
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
        dropdown_level2_dead.select(on_select_dropdown_level2)
        openfield_level2_dead.select(on_select_openfield_level2)
        dropdown_extra_level2_dead.select(on_select_dropdown_extra_level2)
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
        dropdown_level2_wounded.select(on_select_dropdown_level2)
        openfield_level2_wounded.select(on_select_openfield_level2)
        dropdown_extra_level2_wounded.select(on_select_dropdown_extra_level2)
        # ---------------------------------------------------------
        # Radio Behavior Wounded
        radio_behavior_wounded.change(fn=show_behavior,
                                    inputs=[radio_behavior_wounded, gr.Text("wounded", visible=False)],
                                    outputs=[behavior_checkbox, behavior_text])
        behavior_checkbox.select(on_select_behavior, 
                                 inputs=[behavior_checkbox])
        # ---------------------------------------------------------
        # Radio Physical Wounded
        radio_physical_wounded.change(fn=show_physical,
                                    inputs=[radio_physical_wounded, gr.Text("wounded", visible=False)],
                                    outputs=[physical_boxes_wounded])

        # Checkbox Physical Wounded
        physical_boxes_wounded.select(find_bounding_box, 
                        inputs=[physical_boxes_wounded, gr.Textbox(value="wounded", visible=False)], 
                        outputs=[checkbox_beak, text_beak, 
                                 checkbox_body, text_body, 
                                 checkbox_feathers, text_feathers, 
                                 checkbox_head, text_head, 
                                 checkbox_legs, text_legs
                                    ])
        checkbox_beak.select(on_select_body_part, inputs=[checkbox_beak, gr.Text("beak", visible=False)])
        checkbox_body.select(on_select_body_part, inputs=[checkbox_body, gr.Text("body", visible=False)])
        checkbox_feathers.select(on_select_body_part, inputs=[checkbox_feathers, gr.Text("feathers", visible=False)])
        checkbox_head.select(on_select_body_part, inputs=[checkbox_head, gr.Text("head", visible=False)])
        checkbox_legs.select(on_select_body_part, inputs=[checkbox_legs, gr.Text("legs", visible=False)])

        # ---------------------------------------------------------
        # Add One Individual's Data to the Dataframe
        with gr.Row(): 
            button_df = gr.Button("Submit Animal Report", scale = 3)
            button_clear = gr.ClearButton(scale = 1, 
                                          components=[
                location, identified_location, 
                button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead,
                radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded,
                button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                behavior_checkbox, behavior_text, 
                physical_boxes_wounded, 
                checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs
                ])
        button_clear.click()
        button_df.click(save_individual_to_df, 
                        inputs=[df],
                        outputs=[df])
        button_df.click(lambda: Modal(visible=False), None, modal)
    show_modal.click(lambda: Modal(visible=True), None, modal)
    show_modal.click(create_json)


     
     
     
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3333)