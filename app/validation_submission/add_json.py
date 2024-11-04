from validation_submission.create_json import create_json_one_individual, create_tmp
import json 

def add_data_to_individual(key, value): 
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    one_individual[key] = value
    create_json_one_individual(one_individual)

def add_data_tmp(tmp_name, key, value): 
    with open(f"app/assets/tmp_json/tmp_{tmp_name}.json", 'r') as openfile:
        tmp = json.load(openfile)
    tmp[key] = value
    create_tmp(tmp_name, tmp)
    