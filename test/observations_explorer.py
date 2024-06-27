import pandas as pd
from pandas import json_normalize
import json

with open('test/data/observations.json') as f:
    observations = json.load(f)

#---------------------------------------------- One complex example observation

# example_ob = {"date": {"@timestamp": "1719266400", "@notime": "1", "@offset": "7200", "@ISO8601": "2024-06-25T00:00:00+02:00", "#text": "Tuesday, June 25th, 2024"}, 
#            "species": {"@id": "394", "sys_order": "6160", "taxonomy": "1", "rarity": "verycommon", "name": "Black Redstart", "latin_name": "Phoenicurus ochruros", "category": "C", "atlas_13_16": {"@id": "V", "#text": "V"}}, 
#            "place": {"@id": "34089", "name": "Obersiggenthal [665/259]", "altitude": "382", "place_type": "square", "loc_precision": "750", "coord_lat": "47.483001420255", "coord_lon": "8.3076676785656", "municipality": "Obersiggenthal", "county": "AG", "country": ""}, 
#            "observers": [{"@id": "11983", "@uid": "78580", "@vowa_id": "0", "code": "4af09202bb09", "name": "Lena Ottenheimer", "anonymous": "0", "anonymous_in_export": "0", "second_hand": "0", "traid": "11983", "id_sighting": "31212361", "id_universal": "1_31212361", "timing": {"@timestamp": "1719293272", "@notime": "0", "@offset": "7200", "@ISO8601": "2024-06-25T07:27:52+02:00", "#text": "Tuesday, June 25th, 2024, 07:27:52"}, "coord_lat": "47.479646", "coord_lon": "8.307856", "altitude": "382", "atlas_grid_name": "66 25 (Baden)", "precision": "place", "estimation_code": "EXACT_VALUE", "count": "1", "flight_number": "1", "source": "MOBILE_LIVE", "insert_date": {"@timestamp": "1719300787", "@notime": "0", "@offset": "7200", "@ISO8601": "2024-06-25T09:33:07+02:00", "#text": "Tuesday, June 25th, 2024, 09:33:07"}, "details": [{"count": "1", "sex": {"@id": "F", "#text": "female"}, "age": {"@id": "U", "#text": "unknown"}}], "has_death": "2", "extended_info": {"mortality": {"comment": "nicht 100% sichee", "death_cause2": "CRASH", "wounded": "0", "crash_object": "BUILDING"}}}]}


#---------------------------------------------- High level observations info (observer, place, time, species) 
# sightings = observations['data']['sightings']
# df = json_normalize(sightings)
# print(df.columns)

#---------------------------------------------- Mortality info in observations 
mortality_records = []
for ob in observations['data']['sightings']: 
    if "extended_info" in ob["observers"][0].keys(): 
        extended_infos = ob["observers"][0]["extended_info"]
        if "mortality" in extended_infos.keys(): 
            print(extended_infos["mortality"])
            mortality_records.append(extended_infos["mortality"])
df_mortality = pd.DataFrame.from_records(mortality_records)
print(df_mortality.head())