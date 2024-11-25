import json 
from validation_submission.get_json import get_json_all_individuals
from validation_submission.validation import validate_individual

def validate_save_individual(session_state, error_box):
    individual, error_box = validate_individual(session_state, error_box)
    if individual:
        session_state = save_to_all_individuals(session_state, individual.model_dump())
    return session_state, individual, error_box

def save_to_all_individuals(session_state, one_individual):
    all_individuals = get_json_all_individuals(session_state)
    all_individuals[str(len(all_individuals))] = one_individual
    # all_individuals_for_json = json.dumps(all_individuals)
    # with open("data/all_individuals.json", "w") as outfile:
    #     outfile.write(all_individuals_for_json)
    return session_state, all_individuals