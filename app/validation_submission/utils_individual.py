import random
import string
import hashlib

def generate_random_md5():
    # Generate a random string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    # Encode the string and compute its MD5 hash
    md5_hash = hashlib.md5(random_string.encode()).hexdigest()
    return md5_hash

def add_data_to_individual(key, value, individual): 
    individual[key] = value
    return individual


    