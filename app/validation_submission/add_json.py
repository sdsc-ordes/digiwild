from validation_submission.create_json import create_json_one_individual, create_tmp
import json 

# def add_data_to_individual(key, value): 
#     with open("data/one_individual.json", 'r') as openfile:
#         one_individual = json.load(openfile)
#     one_individual[key] = value
#     create_json_one_individual(one_individual)

# def add_data_tmp(tmp_name, key, value): 
#     with open(f"app/assets/tmp_json/tmp_{tmp_name}.json", 'r') as openfile:
#         tmp = json.load(openfile)
#     tmp[key] = value
#     create_tmp(tmp_name, tmp)
    
def add_data_to_individual(state_dict, key, value):
    """
    Add data to one_individual in session state
    Args:
        state_dict: Gradio session state dictionary
        key: Key to add/update
        value: Value to store
    Returns:
        Updated state
    """
    state_dict["one_individual"][key] = value
    return state_dict

def add_data_tmp(state_dict, tmp_name, key, value):
    """
    Add data to temporary storage in session state
    Args:
        state_dict: Gradio session state dictionary
        tmp_name: Name of temporary storage
        key: Key to add/update
        value: Value to store
    Returns:
        Updated state
    """
    if f"tmp_{tmp_name}" not in state_dict:
        state_dict[f"tmp_{tmp_name}"] = {}
    state_dict[f"tmp_{tmp_name}"][key] = value
    return state_dict