import json


def load_notes(file_path):
    with open(file_path, 'r') as file:
        notes = json.load(file)
        return notes