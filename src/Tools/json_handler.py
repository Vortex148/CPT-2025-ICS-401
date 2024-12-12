import json
import os
from src.common_variables import *

def get_json_path(file_name):
    return os.path.join(json_directory, f"{file_name}.json")

# Defining a function that takes an undefined number of parameters.
# These parameters must be key value pairs so the json is updated correctly.
def update_json(file, **kwargs):
    file_path = get_json_path(file)

    with open(file_path, "r") as reading_file:
        data = json.load(reading_file)

    # Defining the change
    for key, value in kwargs.items():
        data[key] = value

    # Writing the change to the file
    with open(file_path, "w") as writing_file:
        json.dump(data, writing_file, indent=4)

# Debugging function that checks the value of desired key.
# For this, *args is used because the parameter is not a pair.
def read_json(file, *args):
    file_path = get_json_path(file)

    # Defining a dictionary and appending the results of the search to it
    results = {}

    with open(file_path, "r") as FILE:
        data = json.load(FILE)

    for x in args:
        results[x] = data.get(x)

    return results
