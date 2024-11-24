import json 
import uuid
from validation_submission.json_data import json_data

def get_session_id():
    # Generate a unique session ID for each user
    return str(uuid.uuid4())

# def create_json_one_individual(one_individual={}):
#     one_individual = json.dumps(one_individual)
#     with open("data/one_individual.json", "w") as outfile:
#         outfile.write(one_individual)

# def create_json_all_individuals(all_individuals={}):
#     all_individuals = json.dumps(all_individuals)
#     with open("data/all_individuals.json", "w") as outfile:
#         outfile.write(all_individuals)

# def create_tmp(tmp_name="wounded_dead", tmp={}):
#     tmp = json.dumps(tmp)
#     with open(f"app/assets/tmp_json/tmp_{tmp_name}.json", "w") as outfile:
#         outfile.write(tmp)

# These changes make the json to stay in memmory. We need to remember to flush it once the session has beeen submitted to the server. 
def create_json_one_individual(session_id, one_individual={}):
    if session_id not in json_data:
        json_data[session_id] = {}
    json_data[session_id]["one_individual"] = one_individual

def create_json_all_individuals(session_id, all_individuals={}):
    if session_id not in json_data:
        json_data[session_id] = {}
    json_data[session_id]["all_individuals"] = all_individuals

def create_tmp(session_id, tmp_name="wounded_dead", tmp={}):
    if session_id not in json_data:
        json_data[session_id] = {}
    if "tmp" not in json_data[session_id]:
        json_data[session_id]["tmp"] = {}
    json_data[session_id]["tmp"][tmp_name] = tmp

def reset_json(session_id): 
    create_json_one_individual(session_id)
    create_tmp(session_id)

# def reset_json(): 
#     create_json_one_individual()
#     create_tmp()