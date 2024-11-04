import json 

def create_json_one_individual(one_individual={}):
    one_individual = json.dumps(one_individual)
    with open("data/one_individual.json", "w") as outfile:
        outfile.write(one_individual)

def create_json_all_individuals(all_individuals={}):
    all_individuals = json.dumps(all_individuals)
    with open("data/all_individuals.json", "w") as outfile:
        outfile.write(all_individuals)

def create_tmp(tmp_name="wounded_dead", tmp={}):
    tmp = json.dumps(tmp)
    with open(f"app/assets/tmp_json/tmp_{tmp_name}.json", "w") as outfile:
        outfile.write(tmp)

def reset_json(): 
    create_json_one_individual()
    create_tmp()