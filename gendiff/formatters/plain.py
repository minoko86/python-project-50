
import json

from gendiff.tree import DELETED, ADDED, NESTED, CHANGED


def make_format(node, path=''):
    output = []
    for item in node:
        if item['type'] == DELETED:
            output.append(f"Property '{path + item['key']}' was removed")
        elif item['type'] == CHANGED and\
                item['value'][0] != item['value'][1]:
            output.append(f"Property '{path + item['key']}' was updated. "
                          f"From {get_string(item['value'][0])} to "
                          f"{get_string(item['value'][1])}")
        elif item['type'] == ADDED:
            output.append(f"Property '{path + item['key']}'"
                          f" was added with value: "
                          f"{get_string(item['value'])}")
        elif item['type'] == NESTED and item['value']:
            output.append(make_format(item['value'],
                                      path=path + item['key'] + '.'))
    return '\n'.join(output)


def get_string(value):
    if isinstance(value, str):
        result = f"'{value}'"
    elif isinstance(value, dict):
        result = '[complex value]'
    elif value is None:
        result = 'null'
    else:
        result = json.dumps(value)

    return result
