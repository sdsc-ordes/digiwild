import gradio as gr
from gradio_modal import Modal

from validation_submission.create_json import create_json_all_individuals, create_json_one_individual, create_tmp, reset_json
from validation_submission.add_json import add_data_to_individual
from validation_submission.validation import reset_error_box
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

from geolocalisation.js_geolocation import js_geocode, display_location

# with gr.Blocks(theme=theme, css=css) as demo:
with gr.Blocks(theme='shivi/calm_seafoam') as demo:
    individual = gr.State({})

#with gr.Blocks() as demo:
    create_json_all_individuals()
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
            def save_image(camera, individual):
                individual = add_data_to_individual("image", camera.tolist(), individual)
                return individual

            camera = gr.Image(elem_id="image")
            camera.input(save_image, inputs=[camera, individual], outputs=[individual])
        # ---------------------------------------------------------
        # Location
        #with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Location")
                gr.Markdown("#### Location (Using address)")
                location = gr.Textbox(visible=True, interactive=True, label="Location of Sighting")
                #display location processing
                identified_location= gr.Textbox(visible=False, interactive=False, 
                                                label="Identified GPS Location")
                with gr.Row():
                    #to submit it
                    submit_location = gr.Button("Get Coordinates using address", 
                                                visible=True, interactive=True, scale=3)
                    submit_location.click(get_location, inputs=[location, individual], outputs=[identified_location, individual])
                    #to clear it
                    clear_location = gr.ClearButton(components=[location, identified_location], 
                                                    visible=True, interactive=True, scale=1
                                                    )
                    clear_location.click()

                # Geolocation
                gr.Markdown("#### Location (Using GPS)")
                location_data = gr.JSON(label="Identified GPS Location")
                hidden_input = gr.Textbox(visible=False, elem_id="textbox_id")
                btn_gpslocation = gr.Button("Get Coordinates using GPS (Permission required)")
                btn_gpslocation.click(None, [], [], js=js_geocode)
                hidden_input.change(display_location, inputs=hidden_input, outputs=location_data)

                
                # Introducing text_box for Species
                gr.Markdown("### General details")
                with gr.Row():
                    specie = gr.Textbox(
                        label="Species (if known)",
                        placeholder="e.g. European Robin, Common Blackbird",
                        info="Enter the species name if you can identify it. If unsure, provide your best guess or general description (e.g. 'small brown bird')",
                        visible=True,
                        interactive=True
                    )

                # Number of individuals
                with gr.Row():
                    num_individuals = gr.Number(
                        label="Number of Individuals",
                        value=1,  # Default value
                        minimum=1,
                        precision=0,  # Only whole numbers
                        info="Enter the number of animals observed",
                        #placeholder="Enter number...",
                        visible=True,
                        interactive=True
                    )

                # Introducing text_box for comments 
                with gr.Row():
                    comments = gr.TextArea(
                        label="Additional Comments",
                        placeholder="Enter any additional observations or notes about the sighting...",
                        info="Optional: Add any relevant details about the animal(s) or circumstances",
                        lines=3,
                        max_lines=5,
                        visible=True,
                        interactive=True
                    )

        
        # ---------------------------------------------------------
         # ---------------------------------------------------------
        # Dead and Wounded Buttons
        gr.Markdown("## The State of the Animal", label="Title")
        gr.Markdown("Please tell us if the animal was wounded / sick or dead.", label="description")
        with gr.Row() as block_form:
            with gr.Column(scale=1):
                butt_wounded = gr.Button("Wounded / Sick", elem_id="wounded")
            with gr.Column(scale=1):
                butt_dead = gr.Button("Dead", elem_id="dead")

        # ---------------------------------------------------------
        # Initiate sections
        section_dead, individual, radio_circumstance_dead, radio_physical_dead,\
            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, \
                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
                    physical_boxes_dead, \
                    checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead, \
                    fe_collection_dropdown_dead, fe_recepient_dropdown_dead, fe_radio_dropdown_dead, fe_answer_dropdown_dead, \
                    fe_name_recipient_dead, fe_collection_ref_dead \
                    = show_section_dead(False, individual)
        
        section_wounded, individual, radio_circumstance_wounded, radio_behavior_wounded, radio_physical_wounded, \
            button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
                    behavior_checkbox, behavior_text, \
                        physical_boxes_wounded, \
                            checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded, \
                            fe_collection_dropdown_wounded, fe_recepient_dropdown_wounded, fe_radio_dropdown_wounded, fe_answer_dropdown_wounded, \
                                fe_name_recipient_wounded, fe_collection_ref_wounded \
                                = show_section_wounded(False, individual)
    
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # Dead Button Logic
        partial_show_section_dead = partial(show_section_dead, True)
        partial_hide_section_wounded = partial(show_section_wounded, False)
        butt_dead.click(partial_show_section_dead, 
                        inputs=[individual], 
                        outputs=[section_dead, 
                                individual,
                                radio_circumstance_dead, radio_physical_dead,
                                button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
                                physical_boxes_dead, \
                                checkbox_beak_dead, text_beak_dead, checkbox_body_dead, text_body_dead, checkbox_feathers_dead, text_feathers_dead, checkbox_head_dead, text_head_dead, checkbox_legs_dead, text_legs_dead, \
                                fe_collection_dropdown_dead, fe_recepient_dropdown_dead, fe_radio_dropdown_dead, fe_answer_dropdown_dead, \
                                fe_name_recipient_dead, fe_collection_ref_dead \
                                ])
        
        butt_dead.click(partial_hide_section_wounded, 
                        inputs=[individual], 
                        outputs=[section_wounded, 
                                individual,
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
        partial_show_section_wounded = partial(show_section_wounded, True)
        partial_hide_section_dead = partial(show_section_dead, False)

        butt_wounded.click(partial_show_section_wounded, 
                        inputs=[individual], 
                        outputs=[section_wounded, 
                                individual,
                                radio_circumstance_wounded, radio_behavior_wounded, radio_physical_wounded,
                                button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded,
                                behavior_checkbox, behavior_text, 
                                physical_boxes_wounded, \
                                checkbox_beak_wounded, text_beak_wounded, checkbox_body_wounded, text_body_wounded, checkbox_feathers_wounded, text_feathers_wounded, checkbox_head_wounded, text_head_wounded, checkbox_legs_wounded, text_legs_wounded, \
                                fe_collection_dropdown_wounded, fe_recepient_dropdown_wounded, fe_radio_dropdown_wounded, fe_answer_dropdown_wounded, \
                                fe_name_recipient_wounded, fe_collection_ref_wounded \
                                ])
        
        butt_wounded.click(partial_hide_section_dead, 
                           inputs=[individual], 
                           outputs=[section_dead, 
                                    individual,
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
        radio_circumstance_dead.change(fn=show_circumstances,
                                inputs=[radio_circumstance_dead, individual],
                                outputs=[button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, individual]
                                )
        
        # Dropdowns Dead
        button_collision_dead.click(dropdown_collision,
                                    inputs=[individual],
                                    outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, individual])
        button_deliberate_destruction_dead.click(dropdown_deliberate_destruction, inputs=[individual], outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, individual])
        button_indirect_destruction_dead.click(dropdown_indirect_destruction, inputs=[individual], outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, individual])
        button_natural_cause_dead.click(dropdown_natural_cause, inputs=[individual], outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, individual])

        dropdown_dead.select(on_select, inputs=[individual], outputs=[dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, individual])
        dropdown_level2_dead.select(on_select_dropdown_level2, inputs=[individual], outputs=[individual] )
        openfield_level2_dead.change(on_change_openfield_level2, inputs=[openfield_level2_dead, individual], outputs=[individual])
        dropdown_extra_level2_dead.select(on_select_dropdown_extra_level2, inputs=[individual], outputs=[individual])
        # ---------------------------------------------------------
        # Radio Physical Dead
        radio_physical_dead.change(fn=show_physical,
                                    inputs=[radio_physical_dead, gr.Text("dead", visible=False), individual],
                                    outputs=[physical_boxes_dead, individual])

        # Checkbox Physical Dead
        physical_boxes_dead.select(find_bounding_box, 
                        inputs=[physical_boxes_dead, gr.Textbox(value="dead", visible=False)], 
                        outputs=[checkbox_beak_dead, text_beak_dead, 
                                 checkbox_body_dead, text_body_dead, 
                                 checkbox_feathers_dead, text_feathers_dead, 
                                 checkbox_head_dead, text_head_dead, 
                                 checkbox_legs_dead, text_legs_dead
                                    ])
        checkbox_beak_dead.select(on_select_body_part, inputs=[checkbox_beak_dead, gr.Text("beak", visible=False), individual], outputs=[individual])
        checkbox_body_dead.select(on_select_body_part, inputs=[checkbox_body_dead, gr.Text("body", visible=False), individual], outputs=[individual])
        checkbox_feathers_dead.select(on_select_body_part, inputs=[checkbox_feathers_dead, gr.Text("feathers", visible=False), individual], outputs=[individual])
        checkbox_head_dead.select(on_select_body_part, inputs=[checkbox_head_dead, gr.Text("head", visible=False), individual], outputs=[individual])
        checkbox_legs_dead.select(on_select_body_part, inputs=[checkbox_legs_dead, gr.Text("legs", visible=False), individual], outputs=[individual])
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # WOUNDED
        # ---------------------------------------------------------
        # Radio Circumstance Wounded
        radio_circumstance_wounded.change(fn=show_circumstances,
                                inputs=[radio_circumstance_wounded, individual],
                                outputs=[button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                            dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, individual]
                                )
        
        # Dropdowns Circumstance Wounded
        button_collision_wounded.click(dropdown_collision,
                                    inputs=[individual],  
                                    outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, individual])
        button_deliberate_destruction_wounded.click(dropdown_deliberate_destruction, inputs=[individual], outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, individual])
        button_indirect_destruction_wounded.click(dropdown_indirect_destruction, inputs=[individual], outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, individual])
        button_natural_cause_wounded.click(dropdown_natural_cause, inputs=[individual], outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, individual])
        
        dropdown_wounded.select(on_select, inputs=[individual], outputs=[dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, individual])
        dropdown_level2_wounded.select(on_select_dropdown_level2, inputs=[individual], outputs=[individual])
        openfield_level2_wounded.change(on_change_openfield_level2, inputs=[openfield_level2_wounded, individual])
        dropdown_extra_level2_wounded.select(on_select_dropdown_extra_level2, inputs=[individual], outputs=[individual])
        # ---------------------------------------------------------
        # Radio Behavior Wounded
        radio_behavior_wounded.change(fn=show_behavior,
                                    inputs=[radio_behavior_wounded, gr.Text("wounded / sick", visible=False), individual],
                                    outputs=[behavior_checkbox, behavior_text, individual])
        behavior_checkbox.select(on_select_behavior, 
                                 inputs=[behavior_checkbox, individual],
                                 outputs=[individual])
        # ---------------------------------------------------------
        # Radio Physical Wounded
        radio_physical_wounded.change(fn=show_physical,
                                    inputs=[radio_physical_wounded, gr.Text("wounded / sick", visible=False), individual],
                                    outputs=[physical_boxes_wounded, individual])

        # Checkbox Physical Wounded
        physical_boxes_wounded.select(find_bounding_box, 
                        inputs=[physical_boxes_wounded, gr.Textbox(value="wounded / sick", visible=False)], 
                        outputs=[checkbox_beak_wounded, text_beak_wounded, 
                                 checkbox_body_wounded, text_body_wounded, 
                                 checkbox_feathers_wounded, text_feathers_wounded, 
                                 checkbox_head_wounded, text_head_wounded, 
                                 checkbox_legs_wounded, text_legs_wounded
                                    ])
        checkbox_beak_wounded.select(on_select_body_part, inputs=[checkbox_beak_wounded, gr.Text("beak", visible=False), individual], outputs=[individual])
        checkbox_body_wounded.select(on_select_body_part, inputs=[checkbox_body_wounded, gr.Text("body", visible=False), individual], outputs=[individual])
        checkbox_feathers_wounded.select(on_select_body_part, inputs=[checkbox_feathers_wounded, gr.Text("feathers", visible=False), individual], outputs=[individual])
        checkbox_head_wounded.select(on_select_body_part, inputs=[checkbox_head_wounded, gr.Text("head", visible=False), individual], outputs=[individual])
        checkbox_legs_wounded.select(on_select_body_part, inputs=[checkbox_legs_wounded, gr.Text("legs", visible=False), individual], outputs=[individual])
        
        # ---------------------------------------------------------
        # Follow Up Events Wounded 
        fe_collection_dropdown_wounded.select(save_fe, inputs=[fe_collection_dropdown_wounded, gr.Textbox("animal collected", visible=False), individual], outputs=[individual])
        fe_recepient_dropdown_wounded.select(save_fe, inputs=[fe_recepient_dropdown_wounded, gr.Textbox("recipient", visible=False), individual],outputs=[individual])
        fe_radio_dropdown_wounded.select(save_fe, inputs=[fe_radio_dropdown_wounded, gr.Textbox("radiography", visible=False), individual],outputs=[individual]) 
        fe_answer_dropdown_wounded.select(save_fe, inputs=[fe_answer_dropdown_wounded, gr.Textbox("given answer", visible=False), individual],outputs=[individual])
        fe_name_recipient_wounded.input(save_fe, inputs=[fe_name_recipient_wounded, gr.Textbox("recipient name", visible=False), individual],outputs=[individual])
        fe_collection_ref_wounded.input(save_fe, inputs=[fe_collection_ref_wounded, gr.Textbox("collection reference", visible=False), individual],outputs=[individual])

        # ---------------------------------------------------------
        # Follow Up Events Dead 
        fe_collection_dropdown_dead.select(save_fe, inputs=[fe_collection_dropdown_dead, gr.Textbox("animal collected", visible=False), individual],outputs=[individual])
        fe_recepient_dropdown_dead.select(save_fe, inputs=[fe_recepient_dropdown_dead, gr.Textbox("recipient", visible=False), individual],outputs=[individual])
        fe_radio_dropdown_dead.select(save_fe, inputs=[fe_radio_dropdown_dead, gr.Textbox("radiography", visible=False), individual],outputs=[individual]) 
        fe_answer_dropdown_dead.select(save_fe, inputs=[fe_answer_dropdown_dead, gr.Textbox("given answer", visible=False), individual],outputs=[individual])
        fe_name_recipient_dead.input(save_fe, inputs=[fe_name_recipient_dead, gr.Textbox("recipient name", visible=False), individual],outputs=[individual])
        fe_collection_ref_dead.input(save_fe, inputs=[fe_collection_ref_dead, gr.Textbox("collection reference", visible=False), individual], outputs=[individual])

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
        button_clear.click(reset_json)

        button_df.click(save_display_individual, 
                        inputs=[gallery, df, error_box, individual],
                        outputs=[gallery, df, error_box, individual]
                        )
        button_close.click(lambda: Modal(visible=False), None, modal)
    
    # ---------------------------------------------------------
    # Event Functions of the landing page buttons
    show_modal.click(lambda: Modal(visible=True), None, modal)
    show_modal.click(create_json_one_individual)
    show_modal.click(create_tmp)
    #submit_button.click(save_and_rest_df, inputs=[df], outputs=[df])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)