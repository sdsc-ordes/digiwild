import gradio as gr

# Function that processes the Textbox input and generates new CheckboxGroups
def generate_checkbox_groups(textbox_input):
    try:
        num_groups = int(textbox_input)
    except ValueError:
        return "Please enter a valid number."

    # Dynamically create a list of CheckboxGroups
    checkbox_groups = []
    for i in range(num_groups):
        checkbox_groups.append(gr.CheckboxGroup(
            choices=["Option 1", "Option 2", "Option 3"], 
            label=f"Checkbox Group {i + 1}",
            interactive=True
        ))
    
    return checkbox_groups

# Function to process the selections of the dynamically created CheckboxGroups
def process_selections(*checkbox_values):
    results = []
    for i, selections in enumerate(checkbox_values):
        selected_options = ', '.join(selections) if selections else 'None'
        results.append(f"Selected options for group {i + 1}: {selected_options}")
    
    return "\n".join(results)

with gr.Blocks() as demo:
    # Textbox for user input to specify the number of CheckboxGroups
    textbox = gr.Textbox(label="Enter the number of Checkbox Groups to create")
    
    # Button to trigger the generation of CheckboxGroups
    generate_button = gr.Button("Generate Checkbox Groups")
    
    # A placeholder for the dynamically generated CheckboxGroups
    dynamic_checkbox_groups = gr.Column()
    
    # Output Textbox to display the results
    output = gr.Textbox(label="Output")

    # Generate CheckboxGroups based on Textbox input
    def update_dynamic_groups(textbox_value):
        groups = generate_checkbox_groups(textbox_value)
        dynamic_checkbox_groups.children = groups
        return dynamic_checkbox_groups

    generate_button.click(
        fn=update_dynamic_groups,
        inputs=textbox,
        outputs=dynamic_checkbox_groups
    )

    # Button to process selections from the dynamically generated CheckboxGroups
    process_button = gr.Button("Submit Selections")
    
    # Process the selections when the second button is clicked
    def process_dynamic_groups(*checkbox_groups):
        return process_selections(*checkbox_groups)
    
    process_button.click(
        fn=process_dynamic_groups,
        inputs=dynamic_checkbox_groups.children,  # Unpack the dynamically generated groups
        outputs=output
    )

demo.launch(server_name="0.0.0.0")