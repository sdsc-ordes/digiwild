import uuid
from pydantic import ValidationError
import gradio as gr

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

def validate_individual(session_state, error_box):
    error_box = reset_error_box(error_box)
    data = get_json_one_individual(session_state)
    data["identifier"] = str(uuid.uuid4())
    if "image" in data.keys():
        img = ImageBase64.to_base64(data["image"])
    else: 
        img = None
    if "geolocalisation" in data.keys():
        geolocalisation = data["geolocalisation"]
    else:
        geolocalisation = None

    error_behavior = None
    error_circumstance = None 
    error_followup = None 
    error_physical = None 
    error_individual = None
    if "wounded_state" not in data or "dead_state" not in data:
        data["wounded_state"] = "No"
        data["dead_state"] = "No"
    if (data["wounded_state"] == "Yes") or (data["dead_state"] == "Yes"):
        data_wounded_dead = get_json_tmp(session_state, "wounded_dead")
        circumstance, error_circumstance = validate_circumstance(data_wounded_dead)
        physical, error_physical = validate_physical(data_wounded_dead)
        followup, error_followup = validate_follow_up(data_wounded_dead)

        if data["wounded_state"]=="Yes":
            print(physical)
            behavior, error_behavior = validate_behavior(data_wounded_dead)
            try : 
                individual = Report(identifier = data["identifier"],
                                    image = img,
                                    geolocalisation = geolocalisation,
                                    wounded_state = data["wounded_state"],
                                    wounded = Wounded(circumstances = circumstance,
                                                        behaviors = behavior,
                                                        physical_anomalies = physical,
                                                        follow_up_events = followup),
                                    dead_state = data["dead_state"])
            except ValidationError as e:
                print(e)
                error_individual = e

        elif data["dead_state"]=="Yes":
            try: 
                individual = Report(identifier = data["identifier"],
                                    image = img,
                                    geolocalisation = geolocalisation,
                                    wounded_state = data["wounded_state"],
                                    dead_state = data["dead_state"],
                                    dead = Dead(circumstances = circumstance,
                                                        physical_anomalies = physical,
                                                        follow_up_events = followup)
                                        )
            except ValidationError as e:
                print(e)
                error_individual = e
    else:
        try: 
            individual = Report(identifier = data["identifier"],
                                    image = img,
                                    geolocalisation = geolocalisation,
                                    wounded_state = data["wounded_state"],
                                    dead_state = data["dead_state"])
        except ValidationError as e:
            print(e)
            error_individual = e
    if error_behavior or error_circumstance or error_followup or error_physical or error_individual:
        error_box = show_error(error_box, error_behavior, error_circumstance, error_followup, error_physical, error_individual)
        individual = None
    else: 
        error_box= gr.Text(label="ALL VALID.", value="Record Registered. You can return to the Display.", visible=True, elem_id="valid")
    return individual, error_box

def show_error(error_box, error_behavior, error_circumstance, error_followup, error_physical, error_individual):
    error_text = ""
    if error_circumstance:
        error_text += f"Error in circumstance: {error_circumstance}\n"
    if error_behavior:
        error_text += f"Error in behavior: {error_behavior}\n"
    if error_physical:
        error_text += f"Error in physical: {error_physical}\n"
    if error_followup:
        error_text += f"Error in follow-up: {error_followup}\n"
    if error_individual:
        error_text += f"Error in individual: {error_individual}\n"
    error_text += "PLEASE CORRECT THESE ERRORS BEFORE SUBMITTING."
    error_box= gr.Text(label="ERROR DETECTED !", value=error_text, visible=True, elem_id="error")
    return error_box

def reset_error_box(error_box):
    error_box = gr.Text(value=None, visible=False)
    return error_box

#### VALIDATION FUNCTIONS
def validate_circumstance(data): 
    circumstance_raw = get_fields(data, "circumstance")
    circumstance_formatted = process_circumstance(circumstance_raw)
    try: 
        Circumstances.model_validate(circumstance_formatted)
        circumstances = Circumstances(**circumstance_formatted)
        error = None
    except ValidationError as e:
        error = e
        print(e)
        circumstances = None
    return circumstances, error
        

def validate_behavior(data): 
    behaviors_raw = get_fields(data, "behaviors")
    behaviors_formatted = process_behaviors(behaviors_raw)
    try:
        Behaviors.model_validate(behaviors_formatted)
        behavior = Behaviors(**behaviors_formatted)
        error = None
    except ValidationError as e:
        print(e)
        print("Validation failed for the behaviors.")
        behavior = None
        error = e
    return behavior, error
        

def validate_physical(data): 
    physical_raw = get_fields(data, "physical")
    physical_formatted = process_physical(physical_raw)
    try: 
        PhysicalAnomalies.model_validate(physical_formatted)
        physical = PhysicalAnomalies(**physical_formatted)
        error = None
    except ValidationError as e:
        print(e)
        print("Validation failed for the physical anomalies.")
        physical = None
        error = e
    return physical, error
        
def validate_follow_up(data):
    followup_raw = get_fields(data, "followup")
    followup_formatted = process_followup(followup_raw)
    try: 
        FollowUpEvents.model_validate(followup_formatted)
        followup = FollowUpEvents(**followup_formatted)
        error = None
    except ValidationError as e:
        print(e)
        print("Validation failed for the follow-up events.")
        followup = None
    return followup, error
    
        
 
