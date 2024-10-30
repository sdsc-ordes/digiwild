from geopy.geocoders import Nominatim
import gradio as gr
from validation_submission.add_json import add_data_to_individual
from geolocalisation.class_geolocalisation import Geolocalisation


def create_geolocalisation_object(lat, long, name): 
    try: 
        geolocalisation = Geolocalisation(
        longitude={"type": "longitude", "value": long},
        latitude={"type": "latitude", "value": lat},
        name=name
        )
    except: 
        print("Pydantic Error for Geolocalisation")
    return geolocalisation

def save_geolocalisation_to_json(geolocalisation): 
    geo_dict = geolocalisation.dict()
    add_data_to_individual("geolocalisation", geo_dict)

def get_location(address):
    try: 
        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")
        
        # entering the location name
        getLoc = loc.geocode(address)
        
        # latitude and longitude
        lat = getLoc.latitude
        lon = getLoc.longitude

        # Save values
        geolocalisation = create_geolocalisation_object(lat, lon, address)
        save_geolocalisation_to_json(geolocalisation)

        #display location processing
        value = "Latitude = " + str(lat) + "\n" + "Longitude = " + str(lon)
        identified_location= gr.Textbox(visible=True, interactive=False, 
                                        label="Identified GPS Location", 
                                        value=value)
        return identified_location
    
    except:
        error = "Please try another less precise location."
        identified_location= gr.Textbox(visible=True, interactive=False, 
                                        label="Identified GPS Location", 
                                        value=error)
        return identified_location