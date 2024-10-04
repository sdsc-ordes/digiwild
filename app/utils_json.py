import json
import gradio as gr

def create_json_one_individual(one_individual={}):
    # Serializing json
    one_individual = json.dumps(one_individual)
    with open("data/one_individual.json", "w") as outfile:
        outfile.write(one_individual)
def create_json_all_individuals(all_individuals={}):
    all_individuals = json.dumps(all_individuals)
    with open("data/all_individuals.json", "w") as outfile:
        outfile.write(all_individuals)

def add_data_to_individual(key, value): 
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    one_individual[key] = value
    create_json_one_individual(one_individual)

def get_json_one_individual():
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    return one_individual

def get_json_all_individuals():
    with open("data/all_individuals.json", "r") as openfile:
        all_individuals = json.load(openfile)
    return all_individuals

def save_to_all_individuals(one_individual):
    all_individuals = get_json_all_individuals()
    all_individuals[str(len(all_individuals))] = one_individual
    all_individuals_for_json = json.dumps(all_individuals)
    with open("data/all_individuals.json", "w") as outfile:
        outfile.write(all_individuals_for_json)
    return all_individuals

# def save_all_individuals(df):
#     all_individuals = df.to_json(orient="records")
#     with open("data/all_individuals.json", "w") as outfile:
#         outfile.write(all_individuals)
    