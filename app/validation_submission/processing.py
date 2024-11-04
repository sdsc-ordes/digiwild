#### PROCESS FUNCTIONS 

def process_circumstance(data):
    fields_to_check = ["option_dropdown", "open_field", "extra"]
    if data["circumstance_radio"] == "Yes":
        for field in fields_to_check:
            if data["circumstance_type"][field+"_label"] == "NA":
                data["circumstance_type"].pop(field+"_label")
            else :
                val = data[f"circumstance_{field}"]
                key = data["circumstance_type"][field+"_label"]
                data["circumstance_type"][key] = val
                data["circumstance_type"].pop(field+"_label")
    # {"circumstance_radio": true, 
    #  "circumstance": "destruction / deliberatly removed", 
    #  "cirumstance_type": {"type": "removal or direct capture", 
    #                       "option_dropdown_label": "method",
    #                       "open_field_label": "NA", 
    #                       "extra_label": "NA"}, 
    # "circumstance_option_dropdown": "Traffic/Trade"}
    return data

def process_behaviors(data):
    # INPUT  : 
    #"behaviors_radio": true, 
    # "behaviors_type": ["Crash, Falling From The Sky", "Neurological"]
    #OUTPUT: 
#     "behaviors_radio": "Yes",
#   "behaviors_type": [
#     {
#       "type": "abnormal breathing",
#       "description": "Problems breathing, breathing sounds"
#     }
    behaviors =[]
    if data["behaviors_radio"] == "Yes":
        for type in data["behaviors_type"]: 
            new_behavior = {}
            new_behavior["type"] = type
            behaviors.append(new_behavior)
        data["behaviors_type"] = behaviors
    return data 

def process_physical(data):
    # INPUT
    # "physical_type_feathers": "feathers", 
    # "physical_anomaly_type_feathers": ["Blood", "Swelling"]}

    # OUTPUT
#     "physical_radio": "Yes",
#   "physical_anomalies_type": [
#     {
#       "type": "beak",
#       "anomaly_type": "deformation"
#     },
#     {
#       "type": "body",
#       "anomaly_type": "fluffed up"
#     },
    body_parts= ["beak", "body", "legs", "feathers/wings/tail", "head incl. eyes"]
    anomalies=[]
    reformatted = {}
    reformatted["physical_radio"] = data["physical_radio"]
    if data["physical_radio"] == "Yes":
        for body_part in body_parts:
            anomaly = {}
            for key, val in data.items(): 
                if "type_"+ body_part in key:
                    anomaly["type"] = body_part
                elif "anomaly_"+ body_part in key:
                    anomaly["anomaly_type"] = val
            if anomaly: 
                anomalies.append(anomaly)
        reformatted["physical_anomalies_type"] = anomalies
    return reformatted

def process_followup(data):
    #     "follow_up_events": [
#     {
#       "type": "animal collected",
#       "option": "Yes"
#     },
#     {
#       "type": "recipient",
#       "option": "Veterinary",
#       "name_recipient": "Dr. Jane Smith"
#     },
#     {
#       "type": "radiography",
#       "option": "Unknown"
#     },
#     {
#       "type": "given answer",
#       "option": "Discussion with the speaker"
#     },
#     {
#       "type": "collection reference",
#       "reference": "Specimen ID: 12345, Collected on 2023-09-15"
#     }
#   ]
    followup_events = []
    for key, val in data.items(): 
        followup_event={}
        type = key.split("followup")[-1]
        option = type.split(" ")[-1]
        followup_event["type"] = type.strip()
        followup_event[option.strip()] = val 
        followup_events.append(followup_event)
    reformatted ={}
    reformatted["follow_up_events"] = followup_events
    return reformatted