import gradio as gr

css = """
.gradio-container {background: url(https://openclipart.org/image/2000px/279687)}
#warning {background-color: #FFCCCB}
.feedback textarea {font-size: 24px !important}
"""

theme = gr.themes.Soft(primary_hue="teal", secondary_hue="teal", neutral_hue="emerald",
                         font=[gr.themes.GoogleFont("Inconsolata"), "Arial", "sans-serif"])