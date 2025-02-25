css_for_error_box = """
#error {background-color: #e82323 !important;
    color: white !important;
    font-weight: bold;}
#valid {background-color: #07e63f !important;
    color: white !important;
    font-weight: bold;}
"""

css_alternative = """
.gradio-container {background: url(https://openclipart.org/image/2000px/279687)}

/* Main background */
body {
    background-color: #3B4C54;
    color: #ffffff; /* Set default text color for contrast */
}

/* Secondary color for headers and panels */
.gradio-container .card,
.gradio-container h1,
.gradio-container h2,
.gradio-container h3,
.gradio-container h4 {
    background-color: #3F543B;
    color: #ffffff; /* Ensuring text is readable */
}




/* Background color for the wounded section */
#wounded {
    background-color: #503B54;
    color: #ffffff; /* Ensures text is readable */
}

/* Olive green color for headers within the wounded section */
#wounded h1,
#wounded h2,
#wounded h3,
#wounded h4,
#wounded h5,
#wounded h6 {
    color: #ffffff; /* Olive green color for header text */
    background-color: #503B54; /* No background color for headers */
}

/* Styling dropdowns within the wounded section */
#wounded select {
    background-color: #3F543B; /* Olive green background */
    color: #ffffff; /* Ensures text is readable */
    border: 1px solid #3B4C54; /* Optional border for consistency */
}

/* Styling checkboxes within the wounded section */
#wounded input[type="checkbox"] {
    accent-color: #3F543B; /* Olive green color for the checkbox */
}

/* Additional checkbox label styling if needed */
#wounded label {
    color: #ffffff; /* Ensures labels are readable */
}





/* Background color for the dead section */
#dead {
    background-color: #54433B;
    color: #ffffff; /* Ensures text is readable */
}

/* Brown color for headers within the dead section */
#dead h1,
#dead h2,
#dead h3,
#dead h4,
#dead h5,
#dead h6 {
    color: #ffffff; /* Olive green color for header text */
    background-color: #54433B; /* No background color for headers */
}


#bird-boxes {background-color: #3B4C54}
#submit {background-color: #abb2bf}
#error {background-color: #e82323}
#valid {background-color: #07e63f}
"""
