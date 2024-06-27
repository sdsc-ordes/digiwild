import json 

from api_config import *
from api_requester import APIRequester


api_requester = APIRequester(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    user_email=USER_MAIL,
    user_pw=USER_PASSWORD,
    api_base='http://www.ornitho.ch/api/'
)


response, _ = api_requester.request(
    method='GET',
    endpoint='observations/search',
    body={"period_choice":"range","date_from":"1.01.2022","date_to":"24.12.2022","species_choice":"all", "has_death": "2"},
    params={}
)


if response:
    with open('test/data/observations.json', 'w') as f:
        json.dump(response, f)
    #print(response)
else:
    print("Failed to retrieve data.")
