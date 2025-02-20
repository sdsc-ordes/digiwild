import gradio as gr
import json
from geolocalisation.maps import (
    create_geolocalisation_object,
    save_geolocalisation_to_json,
)

# JavaScript code to get location and update hidden_input
js_geocode = """
    function() {
        var textbox = document.querySelector('#textbox_id textarea');
        console.log(textbox)
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    var data = {
                        'latitude': position.coords.latitude,
                        'longitude': position.coords.longitude,
                        'accuracy': position.coords.accuracy
                    };
                    console.log("Geolocation data:", data);
                    textbox.value = JSON.stringify(data);
                    textbox.dispatchEvent(new Event('input', { bubbles: true }));
                },
                function(error) {
                    var data = {'error': error.message};
                    console.log("Geolocation error:", data);
                    textbox.value = JSON.stringify(data);
                    textbox.dispatchEvent(new Event('input', { bubbles: true }));
                }
            );
        } else {
            var data = {'error': 'Geolocation is not supported by this browser.'};
            console.log("Geolocation unsupported:", data);
            textbox.value = JSON.stringify(data);
            textbox.dispatchEvent(new Event('input', { bubbles: true }));
        }
    }
"""


def display_location(location_json, individual):
    geo_dict = json.loads(location_json)
    if "latitude" in geo_dict.keys():
        latitude = geo_dict["latitude"]
        longitude = geo_dict["longitude"]
        geolocalisation = create_geolocalisation_object(latitude, longitude, "NA")
        individual = save_geolocalisation_to_json(geolocalisation, individual)
        geo_text = f"Latitude: {latitude} | Longitude: {longitude}"
    else:
        error = geo_dict["error"]
        geo_text = f"Error occured ({error}). Give your browser permission to use your geolocalisation or change browsers."
    locationtext = gr.Textbox(
        geo_text, visible=True, show_label=False, interactive=False
    )
    return locationtext, individual
