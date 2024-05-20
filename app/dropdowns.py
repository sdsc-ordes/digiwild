import gradio as gr

def dropdown_collision():
    return gr.Dropdown(choices=["Road vehicle", "Train", "Aircraft", "Boat", "Other", "Unknown"], label="Collision with a means of transport", interactive=True)

def dropdown_deliberate_destruction():
    return gr.Dropdown(choices=["Hunting", "Trap", "Poisoning", "Removal or direct capture", "Fishing", "Other", "Unkown"], label="Destruction / Deliberatly removed", interactive=True)        

def dropdown_indirect_destruction(): 
    return gr.Dropdown(choices=["pylone and electric grid",
                                "windfarm",
                                "other collision",
                                "fall",
                                "development work",
                                "pollution / contamination",
                                "agricultural net protection",
                                "vegetal / forest work",
                                "other",
                                "unknown"
                                ], label="Indirect destruction", interactive=True)  

def dropdown_natural_cause(): 
    return gr.Dropdown(choices=["predation",
                                "weather",
                                "natural disaster",
                                "nest fall",
                                "stranding due to exhaustion",
                                "disease/parasite",
                                "accidental drowning",
                                "other",
                                "unknown"
                                ], label="Indirect destruction", interactive=True)            
