from validation_submission.get_json import get_json_tmp, get_json_one_individual
from classes import Report
from circumstances.class_circumstance import Circumstances
from behavior.class_behavior import Behaviors
from physical.class_physical import PhysicalAnomalies

def get_fields(data_dict, keyword): 
    extract = {} 
    for key, val in data_dict.items():
        if keyword in key:
            extract[key] = val
    return extract

def validate_individual():
    data = get_json_tmp("wounded_dead")
    circumstance = validate_circumstance(data)
    behaviors = validate_behavior(data)
    validate_physical(data)
    validate_follow_up(data)
    validate_individual()
    pass


def validate_circumstance(data): 
    circumstance_raw = get_fields(data, "circumstance")
    circumstance_formatted = process_circumstance(circumstance_raw)
    if not Circumstances(**circumstance_formatted).validate(): 
        print("Validation failed for the circumstance.")
    else: 
        return Circumstances(**circumstance_formatted)

def process_circumstance(data):
    fields_to_check = ["option_dropdown", "open_field", "extra"]
    for field in fields_to_check:
        if data["circumstance_type"][field+"_label"] == "NA":
            data["circumstance_type"].pop([field+"_label"])
        else :
            key = data[f"circumstance_{field}"]
            val = data["circumstance_type"][field+"_label"]
            data["circumstance_type"][key] = val
            data["circumstance_type"].pop([field+"_label"])
    # {"circumstance_radio": true, 
    #  "circumstance": "destruction / deliberatly removed", 
    #  "cirumstance_type": {"type": "removal or direct capture", 
    #                       "option_dropdown_label": "method",
    #                       "open_field_label": "NA", 
    #                       "extra_label": "NA"}, 
    # "circumstance_option_dropdown": "Traffic/Trade"}
    return data

def validate_behavior(data): 
    behaviors_raw = get_fields(data, "behaviours")
    behaviors_formatted = process_behaviors(behaviors_raw)
    if not Behaviors(**behaviors_formatted).validate(): 
        print("Validation failed for the behaviours.")
    else: 
        return Behaviors(**behaviors_formatted)

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
    for type in data["behaviors_type"]: 
        new_behavior = {}
        new_behavior["type"] = type
        behaviors.append(new_behavior)
    data["behaviors_type"] = behaviors
    return data 

def validate_physical(data): 
    physical_raw = get_fields(data, "physical")
    physical_formatted = process_physical(physical_raw)
    if not PhysicalAnomalies(**physical_formatted).validate(): 
        print("Validation failed for the physical anomalies.")
    else: 
        return PhysicalAnomalies(**physical_formatted)

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

    pass

def validate_follow_up(data):
    pass

def validate_individual():
    individual = get_json_one_individual()
    if not Report(individual).validate(): 
        print("Validation failed for creating the individual report.")
    pass