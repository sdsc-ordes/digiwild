import gradio as gr
from functools import partial
from dead import show_section_dead
from wounded import show_section_wounded
from dropdowns import *
from maps import get_location
from style import *
from theme import theme, css
from followup_events import create_followup_section

with gr.Blocks(theme=theme, css=css) as demo:
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
    # ---------------------------------------------------------

    import random
    import numpy as np  

    section_labels = [
        "apple",
        "banana",
        "carrot",
        "donut",
        "eggplant",
        "fish",
        "grapes",
        "hamburger",
        "ice cream",
        "juice",
    ]

    with gr.Row():
        num_boxes = gr.Slider(0, 5, 2, step=1, label="Number of boxes")
        num_segments = gr.Slider(0, 5, 1, step=1, label="Number of segments")

    with gr.Row():
        img_input = gr.Image()
        img_output = gr.AnnotatedImage(
            color_map={"banana": "#a89a00", "carrot": "#ffae00"}
        )

    section_btn = gr.Button("Identify Sections")
    selected_section = gr.Textbox(label="Selected Section")

    def section(img, num_boxes, num_segments):
        sections = []
        for a in range(num_boxes):
            x = random.randint(0, img.shape[1])
            y = random.randint(0, img.shape[0])
            w = random.randint(0, img.shape[1] - x)
            h = random.randint(0, img.shape[0] - y)
            sections.append(((x, y, x + w, y + h), section_labels[a]))
        for b in range(num_segments):
            x = random.randint(0, img.shape[1])
            y = random.randint(0, img.shape[0])
            r = random.randint(0, min(x, y, img.shape[1] - x, img.shape[0] - y))
            mask = np.zeros(img.shape[:2])
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    dist_square = (i - y) ** 2 + (j - x) ** 2
                    if dist_square < r**2:
                        mask[i, j] = round((r**2 - dist_square) / r**2 * 4) / 4
            sections.append((mask, section_labels[b + num_boxes]))
        return (img, sections)

    section_btn.click(section, [img_input, num_boxes, num_segments], img_output)

    def select_section(evt: gr.SelectData):
        return section_labels[evt.index]

    img_output.select(select_section, None, selected_section)

    # ---------------------------------------------------------
    # ---------------------------------------------------------
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
    section_dead, button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead = show_section_dead(False)
    section_wounded, button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded= show_section_wounded(False)

    # ---------------------------------------------------------
    # Dead Button Logic
    partial_show_section_dead = partial(show_section_dead, True)
    partial_hide_section_wounded = partial(show_section_wounded, False)
    butt_dead.click(partial_show_section_dead, inputs=None, outputs=[section_dead, 
                                                                     button_collision_dead, button_deliberate_destruction_dead, button_indirect_destruction_dead, button_natural_cause_dead, 
                                                                     dropdown_dead, dropdown_level2_dead, openfield_level2_dead, dropdown_extra_level2_dead
                                                                     ])
    butt_dead.click(partial_hide_section_wounded, inputs=None, outputs=[section_wounded, 
                                                                        button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                                                        dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded
                                                                        ])
    # ---------------------------------------------------------
    # Wounded Button Logic
    partial_show_section_wounded = partial(show_section_wounded, True)
    partial_hide_section_dead = partial(show_section_dead, False)
    butt_wounded.click(partial_show_section_wounded, inputs=None, outputs=[section_wounded, 
                                                                        button_collision_wounded, button_deliberate_destruction_wounded, button_indirect_destruction_wounded, button_natural_cause_wounded, 
                                                                        dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded
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
    # Dropdowns Wounded
    button_collision_wounded.click(dropdown_collision,  
                                outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    button_deliberate_destruction_wounded.click(dropdown_deliberate_destruction, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    button_indirect_destruction_wounded.click(dropdown_indirect_destruction, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    button_natural_cause_wounded.click(dropdown_natural_cause, outputs=[dropdown_wounded, dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])
    
    dropdown_wounded.select(on_select, None, [dropdown_level2_wounded, openfield_level2_wounded, dropdown_extra_level2_wounded])

    # ---------------------------------------------------------
    #Submit Button
    with gr.Column(scale=1):
        subbutt = gr.Button("SUBMIT YOUR OBSERVATION TO ORNITHO", 
                            elem_id="submit", 
                            icon="https://cdn.iconscout.com/icon/free/png-256/free-send-2451554-2082560.png",
                            scale=1)
        output_message = gr.Markdown("Thank you, you are a champion of biodiversity conservation !")

    

demo.launch(server_name="0.0.0.0")