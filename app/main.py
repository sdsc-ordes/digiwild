import gradio as gr
from datasets import disable_caching
disable_caching()


from mode_advanced import advanced 
from mode_simple import simple

demo = gr.TabbedInterface([simple, advanced], ["Simple Mode" , "Advanced Reporting"],
                          theme='shivi/calm_seafoam')

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)