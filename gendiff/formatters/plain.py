
import json

from gendiff.tree import DELETED, ADDED, NESTED, CHANGED


# TEMPLATE_ADDED = "Property '{0}' was added with value: {1}"
# TEMPLATE_REMOVED = "Property '{0}' was removed"
# TEMPLATE_UPDATED = "Property '{0}' was updated. From {1} to {2}"
# def make_format(node, path=[]):
#     output = []
#     for item in node:
#         type_node = item.get('type')
#         key = item.get('key')
#         first_value = item.get('first_value')
#         second_value = item.get('second_value')
#         complex = item.get('nested')
#         path.append(key)
#         if type_node is DELETED:
#             output.append(TEMPLATE_REMOVED.format('.'.join(path)))
#         elif type_node is ADDED:
#             output.append(TEMPLATE_ADDED.format
#                           ('.'.join(path), get_string(second_value)))
#         elif type_node is CHANGED:
#             output.append(TEMPLATE_UPDATED.format
#                           ('.'.join(path), get_string(first_value),
#                            get_string(second_value)))
#         elif type_node is NESTED:
#             output.append(make_format(complex, path))
#         path.pop()
#     return '\n'.join(output)
# def make_entry(type, key, first_value, second_value, nested):
#     return {
#         'type': type,
#         'key': key,
#         'first_value': first_value,
#         'second_value': second_value,
#         'nested': nested,
#     }
# def make_format(node, path=''):
#     output = []
#     for item in node:
#         if item['type'] == DELETED:
#             output.append(f"Property '{path + item['key']}' was removed")
#         elif item['type'] == CHANGED and\
#                 item['first_value'] != item['second_value']:
#             output.append(f"Property '{path + item['key']}' was updated. "
#                           f"From {get_string(item['first_value'])} to "
#                           f"{get_string(item['second_value'])}")
#         elif item['type'] == ADDED:
#             output.append(f"Property '{path + item['key']}'"
#                           f" was added with value: "
#                           f"{get_string(item['second_value'])}")
#         elif item['type'] == NESTED and item['nested']:
#             output.append(make_format(item['nested'],
#                                       path=path + item['key'] + '.'))
#     return '\n'.join(output)


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
