from geopy.geocoders import Nominatim
import gradio as gr
from utils_json import add_data_to_individual
 
def get_location(address):
    # try: 
        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")
        
        # entering the location name
        getLoc = loc.geocode(address)
        
        # latitude and longitude
        lat = getLoc.latitude
        lon = getLoc.longitude

        # Save values
        add_data_to_individual("latitude", lat)
        add_data_to_individual("longitude", lon)

        #display location processing
        value = "Latitude = " + str(lat) + "\n" + "Longitude = " + str(lon)
        identified_location= gr.Textbox(visible=True, interactive=False, 
                                        label="Identified GPS Location", 
                                        value=value)
        return identified_location
    
    # except:
    #     error = "Please try another less precise location."
    #     identified_location= gr.Textbox(visible=True, interactive=False, 
    #                                     label="Identified GPS Location", 
    #                                     value=error)
    #     return identified_location