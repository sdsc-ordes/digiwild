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
    return data

def process_behaviors(data):
    behaviors =[]
    if data["behaviors_radio"] == "Yes":
        for type in data["behaviors_type"]: 
            new_behavior = {}
            new_behavior["type"] = type
            behaviors.append(new_behavior)
        data["behaviors_type"] = behaviors
    return data 

def process_physical(data):
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