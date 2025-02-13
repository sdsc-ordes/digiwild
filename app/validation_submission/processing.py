#### PROCESS FUNCTIONS 

def process_circumstance(data):
    print(data)
    fields_to_check = ["option_dropdown", "open_field", "extra"]
    reformatted ={}
    if ("circumstance_radio" in data.keys()) and ("circumstance" in data.keys()) and ("circumstance_type" in data.keys()) and (data["circumstance_radio"] == "Yes"):
        reformatted["circumstance_radio"] = data["circumstance_radio"]
        reformatted["circumstance"] = data["circumstance"]
        reformatted["circumstance_type"] = {}
        for field in fields_to_check:
            if not data["circumstance_type"][field+"_label"] == "NA":
                val = data[f"circumstance_{field}"]
                key = data["circumstance_type"][field+"_label"]
                print("TYPE: ", key)
                reformatted["circumstance_type"][key] = val
    else: 
        reformatted["circumstance_radio"] = None
        reformatted["circumstance"] = None
        reformatted["circumstance_type"] = {}
    print (reformatted)
    return reformatted

def process_behaviors(data):
    behaviors =[]
    reformatted = {}
    if ("behaviors_radio" in data.keys()) and ("behaviors_type" in data.keys()) and (data["behaviors_radio"] == "Yes"):
        reformatted["behaviors_radio"] = data["behaviors_radio"]
        for type in data["behaviors_type"]: 
            new_behavior = {}
            new_behavior["type"] = type
            behaviors.append(new_behavior)
        reformatted["behaviors_type"] = behaviors
    else: 
        reformatted["behaviors_radio"] = None
        reformatted["behaviors_type"] = []
    return reformatted 

def process_physical(data):
    body_parts= ["beak", "body", "legs", "feathers/wings/tail", "head incl. eyes"]
    body_parts_search = ["beak", "body", "legs", "feathers", "head"]
    anomalies=[]
    reformatted = {}
    if ("physical_radio" in data.keys()) and (data["physical_radio"] == "Yes") and any("type_" in key for key in data.keys()) and any("anomaly_" in key for key in data.keys()):
        reformatted["physical_radio"] = data["physical_radio"]
        for b, body_part in enumerate(body_parts_search):
            anomaly = {}
            for key, val in data.items(): 
                if "type_"+ body_part in key:
                    anomaly["type"] = body_parts[b]
                elif "anomaly_"+ body_part in key:
                    anomaly["anomaly_type"] = val
            if anomaly: 
                anomalies.append(anomaly)
        reformatted["physical_anomalies_type"] = anomalies
    else: 
        reformatted["physical_radio"] = None
        reformatted["physical_anomalies_type"] = []
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