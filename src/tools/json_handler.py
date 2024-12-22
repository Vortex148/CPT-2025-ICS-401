import json
import os
from src.common_variables import *
#Todo: create function that reads default values from json and rewrites
# them to the player and weapons json files when the game is quit.
# This way, when the game runs again, the players are given the default ship and weapon.

# Joining the json file name to its directory
# (directories defined in "common_variables.py")
def get_json_path(file_name):
    return os.path.join(json_directory, f"{file_name}.json")

# Defining a function that takes any number of parameters in key-value
# pair format. These keys and values are used to update the json
# Todo: needs to be adjusted so nested key value pairs in json are updated.
def update_json(file, **kwargs):
    file_path = get_json_path(file)

    # Opening the file and copying the data
    with open(file_path, "r") as reading_file:
        data = json.load(reading_file)

    # Changing the desired key value pair(s)
    for key, value in kwargs.items():
        data[key] = value

    # Writing the change(s) back to the file
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
