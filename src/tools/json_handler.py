import json
from src.common_variables import *
from src.Tools.global_tools import get_path

ITEM_SHOP_GROUP = ['players', 'ships', 'weapons']

# Basic loading of json data
def load_json(file):
    file_path = get_path(file, json_directory, "json")

    with open(file_path, 'r') as FILE:
        return json.load(FILE)

# Copying all the json data at the beginning of the program. And
# rewritting it at the end ensures fresh gameplay each time.
def copy_default_json(group=ITEM_SHOP_GROUP):
    global DEFAULT_data
    DEFAULT_data = []

    for file in group:
        DEFAULT_data.append(load_json(file))

# Rewriting command as describe above
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
        # Using . to separate keys from different
        # levels and splicing the path argument at those places
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

# Debugging function: checks the value of desired key (nested or not)
def read_json(file, searches):
    file_path = get_path(file, json_directory, "json")

    # Defining a list and appending the results of the search to it
    results = []

    with open(file_path, "r") as FILE:
        data = json.load(FILE)

    # Same nesting logic as above
    for path in searches:
        keys = path.split(".")
        target = data

        for key in keys:
            target = target.get(key, None)
            if target is None:
                break

        results.append(target)

    return results
