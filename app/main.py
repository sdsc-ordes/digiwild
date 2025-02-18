import gradio as gr
from datasets import disable_caching
disable_caching()


from mode_advanced import advanced 
from mode_simple import simple
from contacts import contacts
from about import about


demo = gr.TabbedInterface([simple, advanced, contacts, about], 
                          ["Simple Mode" , "Advanced Reporting", "Cantonal Contacts", "About"],
                          theme='shivi/calm_seafoam')

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)