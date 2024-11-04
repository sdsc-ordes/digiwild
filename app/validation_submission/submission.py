import json 
from validation_submission.get_json import get_json_all_individuals
from validation_submission.validation import validate_individual

def validate_save_individual():
    individual = validate_individual()
    save_to_all_individuals(individual.model_dump())
    return individual

def save_to_all_individuals(one_individual):
    all_individuals = get_json_all_individuals()
    all_individuals[str(len(all_individuals))] = one_individual
    all_individuals_for_json = json.dumps(all_individuals)
    with open("data/all_individuals.json", "w") as outfile:
        outfile.write(all_individuals_for_json)
    return all_individuals