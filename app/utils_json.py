import json

def create_json(one_individual={}):
    # Serializing json
    one_individual = json.dumps(one_individual)
    # Writing to sample.json
    with open("data/one_individual.json", "w") as outfile:
        outfile.write(one_individual)

def add_data_to_individual(key, value): 
    with open("data/one_individual.json", 'r') as openfile:
        # Reading from json file
        one_individual = json.load(openfile)
    one_individual[key] = value
    create_json(one_individual)

def get_json_one_individual():
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    return one_individual

