import json

""" Load a json file and return it as a dictionary """


def load_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
