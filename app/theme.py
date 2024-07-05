import gradio as gr

css = """
.gradio-container {background: url(https://openclipart.org/image/2000px/279687)}
#image {background-color: #73b9ae}
#dead {background-color: #13422f}
#wounded {background-color: #2d5543}
#buttons-conditions {background-color: #5f7d6e}
#dropdown-conditions {background-color: #92a69c}
#submit {background-color: #333333}
"""


theme = gr.themes.Soft(primary_hue="teal", secondary_hue="teal", neutral_hue="emerald",
                         font=[gr.themes.GoogleFont("Inconsolata"), "Arial", "sans-serif"])