import json 
from validation_submission.get_json import get_json_all_individuals
from validation_submission.validation import validate_individual

def validate_save_individual(data, error_box):
    individual, error_box = validate_individual(data, error_box)
    if individual:
        save_to_all_individuals(individual.model_dump())
    return individual, error_box, data

def save_to_all_individuals(one_individual):
    all_individuals = get_json_all_individuals()
    all_individuals[str(len(all_individuals))] = one_individual
    all_individuals_for_json = json.dumps(all_individuals)
    with open("data/all_individuals.json", "w") as outfile:
        outfile.write(all_individuals_for_json)
    return all_individuals

from huggingface_hub import HfApi
import os 

#save all individuals one by one in JSON wish md5 hash as json name 
def push_to_dataset_hf():
    token = os.environ.get("HF_TOKEN", None)
    api = HfApi(token=token)
    with open("data/all_individuals.json", "r") as f:
            all = json.load(f)
    api.upload_file(
        path_or_fileobj=f.name,
        path_in_repo=path_in_repo,
        repo_id="SDSC/digiwild-dataset",
        repo_type="dataset",
    )