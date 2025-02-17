import gradio as gr

from dotenv import load_dotenv
import os
load_dotenv()
PATH = os.getcwd() + "/"
PATH_ASSETS = os.getenv('PATH_ASSETS')
PATH_ICONS = PATH + PATH_ASSETS + "icons/"

contact_text = """
    # Contacts

    You have an animal alive or dead in front of you and you do not know what to do? 
    Please call the contact below corresponding to your canton. (Cantons are in alphabetical order.)

    ## AG: Aargau
    117 | Departement Bau, Verkehr und Umwelt, Abteilung Wald, Sektion Jagd und Fischerei

    ## AI: Appenzell Innerrhoden
    071 788 92 87 | Bau- und Umweltdepartement, Amt für Umwelt, Fachstelle Jagd und Fischerei	

    ## AR: Appenzell Ausserrhoden
    079 698 19 16 |Departement Bau und Volkswirtschaft, Amt für Raum und Wald, Abteilung Natur und Wildtiere	

    ## BE: Bern
    0800 940 100 | Wirtschafts-, Energie- und Umweltdirektion	

    ## BL: Basel-Landschaft
    061 922 03 66, 061 552 56 59 | Volkswirtschafts- und Gesundheitsdirektion, Amt für Wald und Wild beider Basel	

    ## BS: Basel-Stadt
    061 922 03 66, 061 552 56 59 | Volkswirtschafts- und Gesundheitsdirektion, Amt für Wald und Wild beider Basel	

    ## FR: Fribourg
    026 305 23 31 | Energie, Landwirtschaft und Umwelt, Amt für Wald und Natur, Sektion Fauna, Jagd und Fischerei

    ## GE: Geneva
    022 388 55 00 | Office cantonal de l'agriculture et de la nature, Centrale d'engagement et des transmissions (CET)	

    ## GL: Glarus
    Verwaltung Bau und Umwelt, Umwelt, Wald und Energie, Jagd und Fischerei	

    ## GR: Graubünden
    055 645 66 66 | Amt für Jagd und Fischerei	Jagdbezirke - Über uns

    ## JU: Jura 
    032 420 48 00, 032 420 65 65 | Departement de l'environnement, Office de l'environnement, Chasse et protection de la faune sauvage	

    ## LU: Luzern
    041 248 81 17, 117 | Bau-, Umwelt- und Wirtschaftsdepartement, Landwirtschaft und Wald, Jagd, Wildhut und Jagdaufsicht	

    ## NE: Neuchatel
    032 889 67 80 | Service de la faune, des fôrets et de la nature, faune	

    ## NW: Nidwalden
    041 618 44 66 | Justiz- und Sicherheitsdirektion, Amt für Justiz, Abteilung Jagd und Fischerei	

    ## OW: Obwalden
    041 666 64 76 | Bau- und Raumentwicklungsdepartement, Amt für Wald und Landschaft, Wildtiere und Jagd	

    ## SG: St. Gallen
    117 | Volkwirtschaftsdepartement, Amt für Natur, Jagd und Fischerei	

    ## SH: Schaffhausen
    052 632 74 66 | Departement des Innern, Jagd und Fischerei	

    ## SO: Solothurn
    117| Volkswirtschaftdepartement, Amt für Wald, Jagd und Fischerei

    ## SZ: Schwyz
    041 819 29 29 | Umweltdepartement, Amt für Wald und Natur, Jagd und Wildtiere	

    ## TG: Thurgau
    058 345 61 50 | Jagd- und Fischereiverwaltung	

    ## TI: Ticino
    091 814 28 71 | Divisione dell'ambiente, Ufficio della caccia e della pesca	

    ## UR: Uri
    041 875 2316 | Sicherheitsdirektion, Amt für Forst und Jagd	

    ## VD: Vaud 
    021 557 88 55 | Environnement, Biodiversité et paysage, Police Faune-nature	

    ## VS: Valais
    027 606 70 00, 117 | Umwelt, Energie und Landwirtschaft, Dienststelle für Jagd, Fischerei und Wildtiere	

    ## ZG: Zug
    041 595 41 41 | Natur, Umwelt und Tiere, Arten, Lebensräume, Wildhut und Fischereiaufsicht	

    """


with gr.Blocks(theme='shivi/calm_seafoam') as contacts:
    with gr.Row(scale = 1): 
        gr.Image(PATH_ICONS+"help.png", height=300,
                        interactive=False,
                        show_fullscreen_button = False, show_share_button=False, 
                        show_download_button=False, show_label=False)
        gr.Image(PATH_ICONS+"contact-information.png", height=300,
                        interactive=False,
                        show_fullscreen_button = False, show_share_button=False, 
                        show_download_button=False, show_label=False)
        gr.Image(PATH_ICONS+"question.png", height=300,
                        interactive=False,
                        show_fullscreen_button = False, show_share_button=False, 
                        show_download_button=False, show_label=False)
        
    gr.Markdown(contact_text, show_label=False)

