import gradio as gr

css = """
.gradio-container {background: url(https://openclipart.org/image/2000px/279687)}
#image {background-color: #73b9ae}
#dead {background-color: #333333}
#wounded {background-color: #5e0724}
#buttons-conditions {background-color: #b3b3b3}
#dropdown-conditions {background-color: #b3b3b3}
#followup {background-color: #38241c} 
#submit {background-color: #abb2bf}
"""

#followup 2nd option: #13422f

theme = gr.themes.Soft(primary_hue="teal", secondary_hue="teal", neutral_hue="emerald",
                         font=[gr.themes.GoogleFont("Inconsolata"), "Arial", "sans-serif"])