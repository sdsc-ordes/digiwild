import gradio as gr

with gr.Blocks() as demo:
    table = gr.Dataframe([[1, 2, 3], [4, 5, 6]])
    #gallery = gr.Gallery([("cat.jpg", "Cat"), ("dog.jpg", "Dog")])
    textbox = gr.Textbox("Hello World!")
    statement = gr.Textbox()

    def on_select(evt: gr.SelectData):
        return gr.Textbox(f"You selected {evt.value} at {evt.index} from {evt.target}")

    table.select(on_select, inputs=[table], outputs=[statement])
    #gallery.select(on_select, gallery, statement)
    textbox.select(on_select, inputs=[textbox], outputs=[statement])

demo.launch(server_name="0.0.0.0", server_port=3131)