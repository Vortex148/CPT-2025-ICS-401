import json
from src.common_variables import *
from src.Tools.global_tools import get_path

ITEM_SHOP_GROUP = ['players', 'ships', 'weapons']

# Joining the json file name to its directory
# (directories defined in "common_variables.py")

# Debugging function that checks the value of desired key (nested or not)
def read_json(file, searches):
    file_path = get_path(file, json_directory, "json")

    # Defining a list and appending the results of the search to it
    results = []

    with open(file_path, "r") as FILE:
        data = json.load(FILE)

    for path in searches:
        # If the key is nested, the argument is passed
        # to the function with . to separate data levels
        keys = path.split(".")
        target = data

        # The for loop is used to build the path to the desired key
        for key in keys:
            target = target.get(key, None)
            if target is None:
                break

        results.append(target)

    print(results)
    return results

# Basic loading of json data
def load_json(file):
    file_path = get_path(file, json_directory, "json")

    with open(file_path, 'r') as FILE:
        return json.load(FILE)

# Copy all the json data at the beginning of the program. It is rewritten
# At the end of the program (likely after changes have been made through the item shop)
# so that when the game is re-opened, the players are given default equipment.
def copy_default_json(group=ITEM_SHOP_GROUP):
    global DEFAULT_data
    DEFAULT_data = []
    for file in group:
        DEFAULT_data.append(load_json(file))

# Rewriting json data as described above at the end of the program
def rewrite_default_json(group=ITEM_SHOP_GROUP):
    for i, file in enumerate(group):
        file_path = get_path(file, json_directory, "json")
        rewritting_data = DEFAULT_data[i]
        with open(file_path, 'w') as FILE:
            json.dump(rewritting_data, FILE, indent=4)

# Updating json data (nested or not)
def update_json(file, updates):
    file_path = get_path(file, json_directory, "json")

    # Opening the file and copying the data
    with open(file_path, "r") as reading_file:
        data = json.load(reading_file)

    # Changing the desired key value pair(s)
    for path, value in updates.items():
        # Same nesting logic as in 'read_json'
        keys = path.split(".")
        target = data

        # Building the path to the key by the following format:
        # target[level_1][level_2][level_3] etc...
        for key in keys[:-1]:
            target = target[key]

        target[keys[-1]] = value

    # Writing the change(s) back to the file
    with open(file_path, "w") as writing_file:
        json.dump(data, writing_file, indent=4)