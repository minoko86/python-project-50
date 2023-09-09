import json
# from gendiff.tree import DELETED, ADDED, NESTED, CHANGED, UNCHANGED


def make_format(node):
    return json.dumps(node, indent=2)

# def make_format_in(node):
#     output = []
#     for item in node:
#         if item['type'] == (DELETED or UNCHANGED):
#             output.append({item['key'], item['value']})
#         elif item['type'] is ADDED:
#             output.append(item['key'])
#             output.append(item['value'])
#         elif item['type'] == NESTED and item['value']:
#             output.append(item['key'])
#             output.append(make_format_in(item['value']))
#         elif item['type'] == CHANGED and\
#                 item['value'][0] != item['value'][1]:
#             output.append(item['key'])
#             output.append(item['value'][0])
#             output.append(item['key'])
#             output.append(item['value'][1])
#         else:
#             output.append(item['key'])
#             output.append(item['value'])
#     return output

# def make_format(node):
#     return json.dumps(make_format_in(node), indent=2)
