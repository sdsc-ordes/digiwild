import gradio as gr
from gradio_modal import Modal
import numpy as np

def save_input(input, df):
    #input_value = str(input)
    df_values = np.array(df) # handle empty dataframe case
    new_row = [input, 0, input]  # default 'age' as 0 for now
    df_values = np.vstack([df_values, new_row])
    df = gr.DataFrame(value=df_values)
    return df

with gr.Blocks() as demo:
    with gr.Tab("Tab 1"):
        show_btn = gr.Button("Show Modal")
        df = gr.Dataframe(
            headers=["name", "age", "gender"],
            #datatype=["str", "number", "str"],
            row_count=1,
            col_count=(3, "fixed"),
        )
        show_markdown = gr.Markdown("This is a markdown")
    with Modal(visible=False) as modal:
            input = gr.Textbox(label="Input 1", interactive=True)
            button = gr.Button("Click me")
            button.click(save_input, 
                         inputs=[input, df],
                         outputs=[df])
            button.click(lambda: Modal(visible=False), None, modal)
    show_btn.click(lambda: Modal(visible=True), None, modal)


     
     
     
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3333)