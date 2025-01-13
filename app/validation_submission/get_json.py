import json

def get_json_one_individual():
    with open("data/one_individual.json", 'r') as openfile:
        one_individual = json.load(openfile)
    return one_individual

## TO DO : check this works
import os
def get_json_all_individuals():
    all_animals = os.getfiles("data")
    all_individuals = []
    for animal in all_animals: 
        all_individuals.append(animal)
    return all_individuals

def get_json_tmp(tmp_name):
    with open(f"app/assets/tmp_json/tmp_{tmp_name}.json", "r") as openfile:
        tmp_json = json.load(openfile)
    return tmp_json