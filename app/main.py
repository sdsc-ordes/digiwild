import gradio as gr



# def Dropdown_update(category):
#     print(category)

#     options_a =  ["C","D","E"]
#     options_b = ["C","D","E"]
#     options_c = ["C","D","E"]

#     if category == "category_a":
#         return gr.Dropdown.update(choices=options_a)
#     elif category == "category_b":
#         return gr.Dropdown.update(choices=options_b)
#     elif category == "category_c":
#         return gr.Dropdown.update(choices=options_c)


def truck_dropdown():
    return gr.Dropdown(choices=["A", "B", "C", "D"], label="Dropdown1", interactive=True)

def truckb_dropdown():
    return gr.Dropdown(choices=["F", "W", "Z", "X"], label="Dropdown2", interactive=True)
                

def show_tab():
    with gr.Tab("Dead/Wounded Information"):

        with gr.Row():
            with gr.Column(scale=1):
                img1 = gr.Image(value='./assets/van.png', show_download_button=False, show_label=False)
                butt1 = gr.Button("Violently hit by a drunk driver")
                
            with gr.Column(scale=1):
                img1 = gr.Image(value='./assets/van.png', show_download_button=False, show_label=False)
                butt2 = gr.Button("Violently hit by two drunk drivers")
                

        with gr.Row():
            with gr.Column(scale=1):
                img3 = gr.Image(value='./assets/van.png', show_download_button=False, show_label=False)
                
            with gr.Column(scale=1):
                img4 = gr.Image(value='./assets/van.png', show_download_button=False, show_label=False)
                
        with gr.Row():
            dropdown = gr.Dropdown(choices=["A","B"], label="Dropdown", interactive=True)

    butt1.click(truck_dropdown, outputs=dropdown)
    butt2.click(truckb_dropdown, outputs=dropdown)



with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            title = gr.Markdown("# Welcome to Digiwild", label="Title")
            description = gr.Markdown("Lorem ipsum", label="description")

    with gr.Row():
        with gr.Column(scale=1):
            camera = gr.Image()


    with gr.Column(scale=1):
        radio_dead = gr.Radio(choices=["Wounded", "Dead"], label="State of the animal")
    
    radio_dead.change(show_tab())
    
    with gr.Column(scale=1):
        subbutt = gr.Button("Submit")
        output_message = gr.Markdown("Thank you, you didn't save this one but you could save the next")

    

demo.launch(server_name="0.0.0.0")