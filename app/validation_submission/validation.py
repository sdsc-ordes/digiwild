from validation_submission.get_json import get_json_tmp, get_json_one_individual
from classes import Report
from circumstances.class_circumstance import Circumstance

def get_fields(data_dict, keyword): 
    extract = {} 
    for key, val in data_dict.items():
        if keyword in key:
            extract[key] = val
    return extract

def validate_individual():
    data = get_json_tmp("wounded_dead")
    validate_circumstance(data)
    validate_behavior(data)
    validate_physical(data)
    validate_follow_up(data)
    validate_individual()
    pass


def validate_circumstance(data): 
    circumstance_raw = get_fields(data, "circumstance")
    circumstance_formatted = process_circumstance(circumstance_raw)
    if not Circumstance(circumstance_formatted).validate(): 
        print("Validation failed for the circumstance.")
    pass
def process_circumstance(data):
    pass

def validate_behavior(data): 
    pass

def validate_physical(data): 
    pass

def validate_follow_up(data):
    pass

def validate_individual():
    individual = get_json_one_individual()
    if not Report(individual).validate(): 
        print("Validation failed for creating the individual report.")
    pass