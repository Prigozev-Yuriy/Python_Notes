import json

def save_notes(notes, file_path):
    with open(file_path, 'w') as file:
        json.dump(notes, file, indent=4)