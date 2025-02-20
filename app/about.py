import gradio as gr

from dotenv import load_dotenv
import os

load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv("PATH_ASSETS")
PATH_ICONS = PATH + PATH_ASSETS + "icons/"

credits_text = """
# Credits

This work stemmed from a fruitful collaboration between SDSC and FIWI.

## Scientific Expertise : FIWI from UniBE

From the [Institute for Fish and Wildlife Health, University of Bern](https://www.fiwi.vetsuisse.unibe.ch)
- **Isabelle Wethli**
- **Dr. Mirjam Pewsner**
- **Dr. Saskia Keller**

## Front End Development: SDSC

From the [Swiss Data Science Center](https://www.datascience.ch)
- **Carlos Viviar Rios**
- **Laure Vancauwenberghe**

## How to Contact Us?

Please reach out to FIWI via [their contacts](https://www.fiwi.vetsuisse.unibe.ch/about_us/team/index_eng.html).

## Special Thanks

- **Vogelwarte** for their advice, especially Samuel Wechsler.
- **Biolovision SA**, providers of **ornitho.ch**, for their collaboration: circumstances are matched to their current data collection schema on ornitho.ch

"""

icons_text = """
### Icons' Attributions
(scroll to see all)

Biolovision for the circumstances icons.

flying-doves-group: <a href="https://www.flaticon.com/free-icons/animal" title="animal icons">Animal icons created by Freepik - Flaticon</a>

Pigeon: <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by Freepik - Flaticon</a>

Bird: <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by PLANBSTUDIO - Flaticon</a>

Medical app: <a href="https://www.flaticon.com/free-icons/health" title="health icons">Health icons created by Smashicons - Flaticon</a>

Pin: <a href="https://www.flaticon.com/free-icons/google-maps" title="google maps icons">Google maps icons created by Creatype - Flaticon</a>

Cardiograms: <a href="https://www.flaticon.com/free-icons/medical" title="medical icons">Medical icons created by Freepik - Flaticon</a>

Swallow: <a href="https://www.flaticon.com/free-icons/swallow" title="swallow icons">Swallow icons created by Freepik - Flaticon</a>

Chicken: <a href="https://www.flaticon.com/free-icons/chicken" title="chicken icons">Chicken icons created by Freepik - Flaticon</a>

eye: <a href="https://www.flaticon.com/free-icons/healthcare-and-medical" title="healthcare and medical icons">Healthcare and medical icons created by juicy_fish - Flaticon</a>

neuron: <a href="https://www.flaticon.com/free-icons/neuron" title="neuron icons">Neuron icons created by manshagraphics - Flaticon</a>

impact: <a href="https://www.flaticon.com/free-icons/consequence" title="consequence icons">Consequence icons created by Awicon - Flaticon</a>

schedule: <a href="https://www.flaticon.com/free-icons/follow-up" title="follow up icons">Follow up icons created by iconsitee - Flaticon</a>

Effective: <a href="https://www.flaticon.com/free-icons/cog" title="cog icons">Cog icons created by monkik - Flaticon</a>

correct: <a href="https://www.flaticon.com/fr/icones-gratuites/termine" title="terminé icônes">Terminé icônes créées par kliwir art - Flaticon</a>

supprimer: <a href="https://www.flaticon.com/fr/icones-gratuites/faux" title="faux icônes">Faux icônes créées par hqrloveq - Flaticon</a>

balai-magique: <a href="https://www.flaticon.com/fr/icones-gratuites/la-magie" title="la magie icônes">La magie icônes créées par Freepik - Flaticon</a>

contact-information: <a href="https://www.flaticon.com/free-icons/contact-information" title="contact information icons">Contact information icons created by Freepik - Flaticon</a>

help: <a href="https://www.flaticon.com/free-icons/help" title="help icons">Help icons created by Freepik - Flaticon</a>

question: <a href="https://www.flaticon.com/free-icons/question" title="question icons">Question icons created by Freepik - Flaticon</a>
"""

with gr.Blocks(theme="shivi/calm_seafoam") as about:
    with gr.Row(scale=1):
        gr.Image(
            PATH_ICONS + "sdsc.png",
            height=200,
            interactive=False,
            show_fullscreen_button=False,
            show_share_button=False,
            show_download_button=False,
            show_label=False,
        )
        gr.Image(
            PATH_ICONS + "fiwi.png",
            height=200,
            interactive=False,
            show_fullscreen_button=False,
            show_share_button=False,
            show_download_button=False,
            show_label=False,
        )

    gr.Markdown(credits_text, show_label=False)
    gr.Markdown(icons_text, show_label=False, height=100)
