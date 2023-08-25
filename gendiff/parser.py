import json
import yaml
import os

# def parse(data, format):

#     FORMATS = {
#         'json': json.loads,
#         'yaml': yaml.safe_load,
#         'yml': yaml.safe_load
#     }

#     return FORMATS.get(format)(data)

# def read_file(file_name):

#     with open(file_name, 'r') as file:
#         file_data = file.read()
#         fyle_format = file_name.split('.')[-1]
#         return file_data, fyle_format


def parse(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        extension = os.path.splitext(file_path)[1]
    if extension in (".yml", ".yaml"):
        return yaml.safe_load(data)
    elif extension == ".json":
        return json.loads(data)
    else:
        raise ValueError('Filetype is not supported.')
