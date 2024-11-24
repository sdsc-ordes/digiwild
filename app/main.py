import gradio as gr
import json
from gradio_modal import Modal

from validation_submission.create_json import create_json_all_individuals, create_json_one_individual, create_tmp, reset_json, get_session_id
from validation_submission.add_json import add_data_to_individual
from validation_submission.validation import reset_error_box
from validation_submission.json_data import json_data
from display import save_display_individual
from geolocalisation.maps import get_location
from functools import partial
from dead import show_section_dead
from wounded import show_section_wounded
from circumstances.circumstances import show_circumstances
from circumstances.circumstances_dropdowns import *
from physical.physical_select_animal import show_physical, find_bounding_box
from physical.physical_checkbox import on_select_body_part, hide_physical
from behavior.behavior_checkbox import show_behavior, on_select_behavior
from follow_up.followup_events import save_fe
from styling.style import *
from styling.theme import css


def download_json():
    # Convert json_data to a JSON string
    json_str = json.dumps(json_data, indent=4)
    # Save the JSON string to a file
    with open("json_data.json", "w") as json_file:
        json_file.write(json_str)
    return "json_data.json"

# with gr.Blocks(theme=theme, css=css) as demo:
with gr.Blocks(theme='shivi/calm_seafoam') as demo:
    session_id = get_session_id()
    create_json_all_individuals(session_id)
    # ---------------------------------------------------------
    # Intro Text
    with gr.Row():
        with gr.Column(scale=1):
            title = gr.Markdown("# Welcome to Digiwild", label="Title")
            description = gr.Markdown("Please record your wildlife observations here !", label="description")
    with gr.Row(): 
        show_modal = gr.Button("Add an Animal", scale=3)
        submit_button = gr.Button("Submit All Animals", scale=1)
    df = gr.Dataframe(headers=["Identifier", "Location", "Wounded", "Dead"], visible=False, interactive=False)
    gallery = gr.Gallery(
        label="Gallery of Records", elem_id="gallery", 
        columns=[1], rows=[1],
        object_fit="contain", height="auto", interactive=False)
    
    # Download JSON for debug options
    download_button = gr.Button("Download JSON Data")
    download_file = gr.File(label="Download JSON File", interactive=False)
    download_button.click(download_json, outputs=download_file)

    with Modal(visible=False) as modal:
        # ---------------------------------------------------------
        # Intro Text
        with gr.Row():
            with gr.Column(scale=1):
                title = gr.Markdown("# Animal Report", label="Title")
                description = gr.Markdown("Please record your observation here.", label="description")

        # ---------------------------------------------------------
        # Camera
        with gr.Row():
            def save_image(camera):
                add_data_to_individual(session_id, "image", camera.tolist())

            camera = gr.Image(elem_id="image")
            camera.input(save_image, inputs=[camera])
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
                    get_location_partial = partial(get_location, session_id)
                    submit_location.click(get_location, inputs=[location], outputs=[identified_location])
                    #to clear it
                    clear_location = gr.ClearButton(components=[location, identified_location], 
                                                    visible=True, interactive=True, scale=1
                                                    )
                    clear_location.click()

                # TODO: Introduce text_box for Species

                # TODO: Introduce text_box for comments 

        
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
        section_dead, radio_circumstance_dead, radio_physical_dead,\
            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, \
                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
                    physical_boxes_dead, \
                    checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead, \
                    fe_collection_dropdown_dead, fe_recepient_dropdown_dead, fe_radio_dropdown_dead, fe_answer_dropdown_dead, \
                    fe_name_recipient_dead, fe_collection_ref_dead \
                    = show_section_dead(session_id, False)
        section_wounded, radio_circumstance_wounded, radio_behavior_wounded, radio_physical_wounded, \
            button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
                    behavior_checkbox, behavior_text, \
                        physical_boxes_wounded, \
                            checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded, \
                            fe_collection_dropdown_wounded, fe_recepient_dropdown_wounded, fe_radio_dropdown_wounded, fe_answer_dropdown_wounded, \
                                fe_name_recipient_wounded, fe_collection_ref_wounded \
                                = show_section_wounded(session_id, False)
    
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # Dead Button Logic
        partial_show_section_dead = partial(show_section_dead, session_id, True)
        partial_hide_section_wounded = partial(show_section_wounded, session_id, False)
        butt_dead.click(partial_show_section_dead, 
                        inputs=None, 
                        outputs=[section_dead, 
                                radio_circumstance_dead, radio_physical_dead,
                                button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
                                physical_boxes_dead, \
                                checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead, \
                                fe_collection_dropdown_dead, fe_recepient_dropdown_dead, fe_radio_dropdown_dead, fe_answer_dropdown_dead, \
                                fe_name_recipient_dead, fe_collection_ref_dead \
                                ])
        butt_dead.click(partial_hide_section_wounded, 
                        inputs=None, 
                        outputs=[section_wounded, 
                                radio_circumstance_wounded, radio_behavior_wounded, radio_physical_wounded,
                                button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                                behavior_checkbox, behavior_text, 
                                physical_boxes_wounded, \
                                checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded, \
                                fe_collection_dropdown_wounded, fe_recepient_dropdown_wounded, fe_radio_dropdown_wounded, fe_answer_dropdown_wounded, \
                                fe_name_recipient_wounded, fe_collection_ref_wounded \
                                ])
        
        # ---------------------------------------------------------
        # Wounded Button Logic
        partial_show_section_wounded = partial(show_section_wounded, session_id, True)
        partial_hide_section_dead = partial(show_section_dead, session_id, False)

        butt_wounded.click(partial_show_section_wounded, 
                        inputs=None, 
                        outputs=[section_wounded, 
                                    radio_circumstance_wounded, radio_behavior_wounded, radio_physical_wounded,
                                    button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                    dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                                    behavior_checkbox, behavior_text, 
                                    physical_boxes_wounded, \
                                    checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded, \
                                    fe_collection_dropdown_wounded, fe_recepient_dropdown_wounded, fe_radio_dropdown_wounded, fe_answer_dropdown_wounded, \
                                    fe_name_recipient_wounded, fe_collection_ref_wounded \
                                    ])
        butt_wounded.click(partial_hide_section_dead, inputs=None, outputs=[section_dead, 
                                                                            radio_circumstance_dead, radio_physical_dead,
                                                                            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                                                            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
                                                                            physical_boxes_dead, \
                                                                            checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead, \
                                                                            fe_collection_dropdown_dead, fe_recepient_dropdown_dead, fe_radio_dropdown_dead, fe_answer_dropdown_dead, \
                                                                            fe_name_recipient_dead, fe_collection_ref_dead \
                                                                            ])
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # DEAD
        # ---------------------------------------------------------
        # Radio Circumstance Dead
        show_circumstances_partial = partial(show_circumstances, session_id)
        radio_circumstance_dead.change(fn=show_circumstances_partial,
                                inputs=[radio_circumstance_dead],
                                outputs=[button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead]
                                )
        
        # Dropdowns Dead
        button_collision_dead.click(dropdown_collision,  
                                    outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        button_deliberate_destruction_dead.click(dropdown_deliberate_destruction, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        button_indirect_destruction_dead.click(dropdown_indirect_destruction, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        button_natural_cause_dead.click(dropdown_natural_cause, outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])

        dropdown_dead.select(on_select, None, [dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])
        dropdown_level2_dead.select(on_select_dropdown_level2)
        openfield_level2_dead.change(on_change_openfield_level2, inputs=[openfield_level2_dead])
        dropdown_extra_level2_dead.select(on_select_dropdown_extra_level2)
        # ---------------------------------------------------------
        # Radio Physical Dead
        show_physical_partial = partial(show_physical, session_id)
        radio_physical_dead.change(fn=show_physical_partial,
                                    inputs=[radio_physical_dead, gr.Text("dead", visible=False)],
                                    outputs=[physical_boxes_dead])

        # Checkbox Physical Dead
        physical_boxes_dead.select(find_bounding_box, 
                        inputs=[physical_boxes_dead, gr.Textbox(value="dead", visible=False)], 
                        outputs=[checkbox_beak_dead, text_beak_dead, 
                                 checkbox_body_dead, text_body_dead, 
                                 checkbox_feathers_dead, text_feathers_dead, 
                                 checkbox_head_dead, text_head_dead, 
                                 checkbox_legs_dead, text_legs_dead
                                    ])
        
        on_select_body_part_partial = partial(on_select_body_part, session_id)
        checkbox_beak_dead.select(on_select_body_part_partial, inputs=[checkbox_beak_dead, gr.Text("beak", visible=False)])
        checkbox_body_dead.select(on_select_body_part_partial, inputs=[checkbox_body_dead, gr.Text("body", visible=False)])
        checkbox_feathers_dead.select(on_select_body_part_partial, inputs=[checkbox_feathers_dead, gr.Text("feathers", visible=False)])
        checkbox_head_dead.select(on_select_body_part_partial, inputs=[checkbox_head_dead, gr.Text("head", visible=False)])
        checkbox_legs_dead.select(on_select_body_part_partial, inputs=[checkbox_legs_dead, gr.Text("legs", visible=False)])
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # WOUNDED
        # ---------------------------------------------------------
        # Radio Circumstance Wounded
        show_circumstances_partial = partial(show_circumstances, session_id)
        radio_circumstance_wounded.change(fn=show_circumstances,
                                inputs=[radio_circumstance_wounded],
                                outputs=[button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                            dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded]
                                )
        
        # Dropdowns Circumstance Wounded
        dropdown_collision_partial = partial(dropdown_collision, session_id)
        button_collision_wounded.click(dropdown_collision_partial,  
                                    outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        dropdown_deliberate_destruction_partial = partial(dropdown_deliberate_destruction, session_id)
        button_deliberate_destruction_wounded.click(dropdown_deliberate_destruction_partial, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        
        dropdown_indirect_destruction_partial = partial(dropdown_indirect_destruction, session_id)
        button_indirect_destruction_wounded.click(dropdown_indirect_destruction_partial, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        
        dropdown_natural_cause_partial = partial(dropdown_natural_cause, session_id)
        button_natural_cause_wounded.click(dropdown_natural_cause_partial, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        
        on_select_partial = partial(on_select, session_id)
        dropdown_wounded.select(on_select_partial, None, [dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
        
        on_select_dropdown_level2_partial = partial(on_select_dropdown_level2, session_id)
        dropdown_level2_wounded.select(on_select_dropdown_level2_partial)

        on_change_openfield_level2_partial = partial(on_change_openfield_level2, session_id)
        openfield_level2_wounded.change(on_change_openfield_level2_partial, inputs=[openfield_level2_wounded])
        
        on_select_dropdown_extra_level2_partial = partial(on_select_dropdown_extra_level2, session_id)
        dropdown_extra_level2_wounded.select(on_select_dropdown_extra_level2)
        # ---------------------------------------------------------
        # Radio Behavior Wounded
        show_behavior_partial = partial(show_behavior, session_id)
        radio_behavior_wounded.change(fn=show_behavior,
                                    inputs=[radio_behavior_wounded, gr.Text("wounded", visible=False)],
                                    outputs=[behavior_checkbox, behavior_text])
        on_select_behavior_partial = partial(on_select_behavior, session_id)
        behavior_checkbox.select(on_select_behavior, 
                                 inputs=[behavior_checkbox])
        # ---------------------------------------------------------
        # Radio Physical Wounded
        show_physical_partial = partial(show_physical, session_id)
        radio_physical_wounded.change(fn=show_physical_partial,
                                    inputs=[radio_physical_wounded, gr.Text("wounded", visible=False)],
                                    outputs=[physical_boxes_wounded])

        # Checkbox Physical Wounded
        physical_boxes_wounded.select(find_bounding_box, 
                        inputs=[physical_boxes_wounded, gr.Textbox(value="wounded", visible=False)], 
                        outputs=[checkbox_beak_wounded, text_beak_wounded, 
                                 checkbox_body_wounded, text_body_wounded, 
                                 checkbox_feathers_wounded, text_feathers_wounded, 
                                 checkbox_head_wounded, text_head_wounded, 
                                 checkbox_legs_wounded, text_legs_wounded
                                    ])
        
        on_select_body_part_partial = partial(on_select_body_part, session_id)
        checkbox_beak_wounded.select(on_select_body_part_partial, inputs=[checkbox_beak_wounded, gr.Text("beak", visible=False)])
        checkbox_body_wounded.select(on_select_body_part_partial, inputs=[checkbox_body_wounded, gr.Text("body", visible=False)])
        checkbox_feathers_wounded.select(on_select_body_part_partial, inputs=[checkbox_feathers_wounded, gr.Text("feathers", visible=False)])
        checkbox_head_wounded.select(on_select_body_part_partial, inputs=[checkbox_head_wounded, gr.Text("head", visible=False)])
        checkbox_legs_wounded.select(on_select_body_part_partial, inputs=[checkbox_legs_wounded, gr.Text("legs", visible=False)])
        
        # ---------------------------------------------------------
        # Follow Up Events Wounded
        save_fe_partial = partial(save_fe, session_id)
        fe_collection_dropdown_wounded.select(save_fe_partial, inputs=[fe_collection_dropdown_wounded, gr.Textbox("animal collected", visible=False)])
        fe_recepient_dropdown_wounded.select(save_fe_partial, inputs=[fe_recepient_dropdown_wounded, gr.Textbox("recipient", visible=False)])
        fe_radio_dropdown_wounded.select(save_fe_partial, inputs=[fe_radio_dropdown_wounded, gr.Textbox("radiography", visible=False)]) 
        fe_answer_dropdown_wounded.select(save_fe_partial, inputs=[fe_answer_dropdown_wounded, gr.Textbox("given answer", visible=False)])
        fe_name_recipient_wounded.input(save_fe_partial, inputs=[fe_name_recipient_wounded, gr.Textbox("recipient name", visible=False)])
        fe_collection_ref_wounded.input(save_fe_partial, inputs=[fe_collection_ref_wounded, gr.Textbox("collection reference", visible=False)])

        # ---------------------------------------------------------
        # Follow Up Events Dead 
        fe_collection_dropdown_dead.select(save_fe_partial, inputs=[fe_collection_dropdown_dead, gr.Textbox("animal collected", visible=False)])
        fe_recepient_dropdown_dead.select(save_fe_partial, inputs=[fe_recepient_dropdown_dead, gr.Textbox("recipient", visible=False)])
        fe_radio_dropdown_dead.select(save_fe_partial, inputs=[fe_radio_dropdown_dead, gr.Textbox("radiography", visible=False)]) 
        fe_answer_dropdown_dead.select(save_fe_partial, inputs=[fe_answer_dropdown_dead, gr.Textbox("given answer", visible=False)])
        fe_name_recipient_dead.input(save_fe_partial, inputs=[fe_name_recipient_dead, gr.Textbox("recipient name", visible=False)])
        fe_collection_ref_dead.input(save_fe_partial, inputs=[fe_collection_ref_dead, gr.Textbox("collection reference", visible=False)])

        # ---------------------------------------------------------
        # Error Box
        error_box = gr.Text(value=None, visible=False)

        # ---------------------------------------------------------
        # Add One Individual's Data to the Dataframe
        # And Allow clearing of all previous output
        with gr.Row(): 
            button_df = gr.Button("Submit Animal Report", scale = 3)
            button_clear = gr.ClearButton(scale = 1, 
                                          components=[
                camera,
                location, identified_location, 
                #dead reset
                radio_circumstance_dead, radio_physical_dead,
                button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead,
                physical_boxes_dead,
                checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead, 
                fe_collection_dropdown_dead, fe_recepient_dropdown_dead, fe_radio_dropdown_dead, fe_answer_dropdown_dead, 
                fe_name_recipient_dead, fe_collection_ref_dead,
                #wounded reset
                radio_circumstance_wounded, radio_behavior_wounded, radio_physical_wounded,
                button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                behavior_checkbox, behavior_text, 
                physical_boxes_wounded, 
                checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded,
                fe_collection_dropdown_wounded, fe_recepient_dropdown_wounded, fe_radio_dropdown_wounded, fe_answer_dropdown_wounded, 
                fe_name_recipient_wounded, fe_collection_ref_wounded,
                error_box
                ])
            button_close = gr.Button("Back to Display", scale = 1)
            

        # ---------------------------------------------------------
        # Button Click Logic
        button_clear.click()
        button_clear.click(hide_physical,
                           outputs=[checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded])
        button_clear.click(hide_physical,
                           outputs=[checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead])
                
        button_clear.click(reset_error_box, inputs=[error_box], outputs=[error_box])
        button_clear.click(reset_json(session_id=session_id))

        button_df.click(save_display_individual, 
                        inputs=[gallery, df, error_box],
                        outputs=[gallery, df, error_box]
                        )
        button_close.click(lambda: Modal(visible=False), None, modal)
    
    # ---------------------------------------------------------
    # Event Functions of the landing page buttons
    show_modal.click(lambda: Modal(visible=True), None, modal)
    show_modal.click(create_json_one_individual(session_id))
    show_modal.click(create_tmp(session_id))
    #submit_button.click(save_and_rest_df, inputs=[df], outputs=[df])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)