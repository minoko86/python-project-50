import json
import yaml
import os


def load_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        extension = os.path.splitext(file_path)[1]
    if extension in (".yml", ".yaml"):
        return yaml.safe_load(data)
    elif extension == ".json":
        return json.loads(data)
    else:
        raise ValueError('Filetype is not supported.')
