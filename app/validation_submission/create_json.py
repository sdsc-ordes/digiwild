import json 

import random
import string

import hashlib

def generate_random_md5():
    # Generate a random string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    # Encode the string and compute its MD5 hash
    md5_hash = hashlib.md5(random_string.encode()).hexdigest()
    return md5_hash

def create_json_one_individual(one_individual={}):
    one_individual["image_md5"] = generate_random_md5()
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