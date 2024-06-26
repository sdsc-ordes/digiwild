import ornitho
from api_config import *

# run python test/ornitho_api.py 

ornitho.consumer_key = CONSUMER_KEY
ornitho.consumer_secret = CONSUMER_SECRET
ornitho.user_email = USER_MAIL
ornitho.user_pw = USER_PASSWORD
ornitho.api_base = "https://www.ornitho.de/api/"

resp = ornitho.Observation.search_all(period_choice="range", date_from="01.10.2019", date_to="31.10.2019")
print(resp)