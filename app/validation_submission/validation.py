import uuid

from validation_submission.get_json import get_json_tmp, get_json_one_individual
from circumstances.class_circumstance import Circumstances
from behavior.class_behavior import Behaviors
from physical.class_physical import PhysicalAnomalies
from follow_up.class_follow_up import FollowUpEvents
from classes import Report, Wounded, Dead, ImageBase64
from validation_submission.processing import process_circumstance, process_behaviors, process_physical, process_followup

def get_fields(data_dict, keyword): 
    extract = {} 
    for key, val in data_dict.items():
        if keyword in key:
            extract[key] = val
    return extract

def validate_individual():
    data = get_json_one_individual()
    data["identifier"] = str(uuid.uuid4())
    if "wounded_state" not in data or "dead_state" not in data:
        data["wounded_state"] = "No"
        data["dead_state"] = "No"
    if (data["wounded_state"] == "Yes") or (data["dead_state"] == "Yes"):
        data_wounded_dead = get_json_tmp("wounded_dead")
        circumstance = validate_circumstance(data_wounded_dead)
        physical = validate_physical(data_wounded_dead)
        followup = validate_follow_up(data_wounded_dead)

        if data["wounded_state"]=="Yes":
            behavior = validate_behavior(data_wounded_dead)
            individual = Report(identifier = data["identifier"],
                                image = ImageBase64.to_base64(data["image"]),
                                geolocalisation = data["geolocalisation"],
                                wounded_state = data["wounded_state"],
                                wounded = Wounded(circumstances = circumstance,
                                                    behaviors = behavior,
                                                    physical_anomalies = physical,
                                                    follow_up_events = followup),
                                dead_state = data["dead_state"])
        elif data["dead_state"]=="Yes":
            individual = Report(identifier = data["identifier"],
                                image = ImageBase64.to_base64(data["image"]),
                                geolocalisation = data["geolocalisation"],
                                wounded_state = data["wounded_state"],
                                dead_state = data["dead_state"],
                                dead = Dead(circumstances = circumstance,
                                                    physical_anomalies = physical,
                                                    follow_up_events = followup)
                                    )
    else:
        data["image"] = ImageBase64.to_base64(data["image"])
        if not Report(**data).validate(): 
            print("Validation failed for creating the individual report.")
        else:
            individual = Report(**data)
    return individual



#### VALIDATION FUNCTIONS
def validate_circumstance(data): 
    circumstance_raw = get_fields(data, "circumstance")
    circumstance_formatted = process_circumstance(circumstance_raw)
    if not Circumstances.model_validate(circumstance_formatted): 
        print("Validation failed for the circumstance.")
    else: 
        return Circumstances(**circumstance_formatted)

def validate_behavior(data): 
    behaviors_raw = get_fields(data, "behaviors")
    behaviors_formatted = process_behaviors(behaviors_raw)
    try:
        Behaviors.model_validate(behaviors_formatted)
        return Behaviors(**behaviors_formatted)
    except: 
        print("Validation failed for the behaviors.")
        

def validate_physical(data): 
    physical_raw = get_fields(data, "physical")
    physical_formatted = process_physical(physical_raw)
    try: 
        PhysicalAnomalies.model_validate(physical_formatted)
        return PhysicalAnomalies(**physical_formatted)
    except:
        print("Validation failed for the physical anomalies.")
        
def validate_follow_up(data):
    followup_raw = get_fields(data, "followup")
    followup_formatted = process_followup(followup_raw)
    try: 
        FollowUpEvents.model_validate(followup_formatted)
        return FollowUpEvents(**followup_formatted)
    except:
        print("Validation failed for the follow-up events.")
    
        
 
