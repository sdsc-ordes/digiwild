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

def display_location(location_json):
    return location_json