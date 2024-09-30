import json
import gradio as gr

def create_json(one_individual={}):
    # Serializing json
    one_individual = json.dumps(one_individual)
    with open("data/one_individual.json", "w") as outfile:
        outfile.write(one_individual)

def add_data_to_individual(key, value): 
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    one_individual[key] = value
    create_json(one_individual)

def get_json_one_individual():
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    return one_individual


def save_all_animals(df):
    all_animals = df.to_json(orient="records")
    with open("data/all_animals.json", "w") as outfile:
        outfile.write(all_animals)
    