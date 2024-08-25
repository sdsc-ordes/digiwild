import gradio as gr
import asyncio
from functools import partial

from dead import show_section_dead
from wounded import show_section_wounded
from circumstances_dropdowns import *

def partial_show_section_wounded():
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
                            = show_section_wounded(True)
    return section_dead, \
            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, \
            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
            section_wounded, radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded, \
            button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
            dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
            behavior_checkbox, behavior_text, \
            physical_boxes_wounded, \
            checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs

def partial_show_section_dead():
    section_wounded, radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded, \
            button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
                dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
                    behavior_checkbox, behavior_text, \
                        physical_boxes_wounded, \
                            checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs \
                            = show_section_wounded(False)
    # Your logic here to show the sections and buttons
    section_dead, \
            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, \
            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead \
            = show_section_dead(True)
    return section_dead, \
            button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, \
            dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead, \
            section_wounded, radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded, \
            button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
            dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
            behavior_checkbox, behavior_text, \
            physical_boxes_wounded, \
            checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs \
                            

def create_animal_tab(num_animals):
    for animal_index in range(int(num_animals)):
        with gr.Tab(f"Animal {animal_index + 1}"):
            # ---------------------------------------------------------
            # Dead and Wounded Buttons
            gr.Markdown("## The State of the Animal", label="Title")
            gr.Markdown("Please tell us if the animal was wounded or dead.", label="description")
            with gr.Row() as block_form:
                with gr.Column(scale=1):
                    butt_wounded = gr.Button("Wounded", elem_id=f"wounded_{animal_index + 1}")
                with gr.Column(scale=1):
                    butt_dead = gr.Button("Dead", elem_id=f"dead_{animal_index + 1}")

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
            # Dead Button Logic for the current tab
            butt_dead.click(partial(partial_show_section_dead),
                            inputs=None, 
                            outputs=[section_dead, 
                                    button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                    dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead,
                                    section_wounded, radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded, \
                                    button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
                                    dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
                                    behavior_checkbox, behavior_text, \
                                    physical_boxes_wounded, \
                                    checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs \
                                ])
            butt_wounded.click(partial(partial_show_section_wounded),
                            inputs=None, 
                            outputs=[section_dead, 
                                    button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                    dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead,
                                    section_wounded, radio_cause_wounded, radio_behavior_wounded, radio_physical_wounded, \
                                    button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, \
                                    dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded, \
                                    behavior_checkbox, behavior_text, \
                                    physical_boxes_wounded, \
                                    checkbox_beak, text_beak, checkbox_body, text_body, checkbox_feathers, text_feathers, checkbox_head, text_head, checkbox_legs, text_legs \
                                ])
            # ---------------------------------------------------------
            # Dead Button Logic for the current tab
            button_collision_dead.click(dropdown_collision, 
                                        outputs=[dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead])


# Initialize global variables
NUM_ANIMALS = 1
VARIABLE_CHANGE_EVENT = asyncio.Event()

# Function to change the global variable
def change_num_animal(num_animals):
    NUM_ANIMALS = int(num_animals)
    print(f"Number animals: {NUM_ANIMALS}")
    VARIABLE_CHANGE_EVENT.set()



# Async function that waits for the global variable to change and then creates tabs
async def tabbify():
    while True: 
        await VARIABLE_CHANGE_EVENT.wait()
        print("Creating tabs!")
        # Simulate tab creation logic
        create_animal_tab(NUM_ANIMALS)


async def main():

    asyncio.create_task(tabbify())

    with gr.Blocks() as demo:
        

        # Input box to enter the number of tabs
        num_tabs = gr.Textbox(label="Enter number of animals:", value="1", interactive=True)
        
        # Button to trigger the generation of tabs
        generate_button = gr.Button("Generate Tabs")
        
        # When the button is clicked, change the global variable
        generate_button.click(fn=change_num_animal, inputs=[num_tabs], outputs=[])
    demo.launch(server_name="0.0.0.0", server_port=5000)

# Run the main function
asyncio.run(main())

