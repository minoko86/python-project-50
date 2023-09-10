import json
from gendiff.tree import DELETED, ADDED, NESTED, UNCHANGED, CHANGED

# def make_format(node):
#     return json.dumps(node, indent=2)


def make_format(data):
    return json.dumps(get_clean_diff(data), indent=2)


def sort_diff(diff_tree):
    sorted_dict = sorted(diff_tree, key=lambda d: d['key'])
    for item in sorted_dict:
        if item['type'] == NESTED:
            item['value'] = sort_diff(item['value'])
    return sorted_dict


def get_clean_diff(node):
    clean_diff = []
    for item in node:
        clean_node = {
            'type': item['type'],
            'key': item['key']
        }
        if item['type'] == DELETED\
                or item['type'] == UNCHANGED:
            clean_node['first_value'] = item['value']
        if item['type'] == ADDED:
            clean_node['second_value'] = item['value']
        if item['type'] == CHANGED:
            clean_node['first_value'] = item['value'][0]
            clean_node['second_value'] = item['value'][1]
        if item['type'] == NESTED:
            clean_node['value'] = get_clean_diff(item['value'])

        clean_diff.append(clean_node)

    return sort_diff(clean_diff)





# def make_format(node):
#     output = []
#     for item in node:
#         if item['type'] == DELETED:
#             output.append({'key': item['key'], 'value': item['value']})
#         elif item['type'] == CHANGED and\
#                 item['value'][0] != item['value'][1]:
#             output.append({'type': CHANGED, 'key': item['key'], 'value': item['value'][0]})
#             output.append({'key': item['key'], 'value': item['value'][1]})
#         elif item['type'] == ADDED:
#             output.append({'key': item['key'], 'value': item['value']})
#         elif item['type'] == NESTED and item['value']:
#             output.append(make_format({'key': item['key'], 'value': item['value']}))  
#     return output


# def make_format(node):
#     return json.dumps(make_format2(node), indent=2)