DELETED = 'deleted'
ADDED = 'added'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
NESTED = 'nested'

def build_diff(data1, data2):
    nodes = []
    first_keys = data1.keys()
    second_keys = data2.keys()
    keys = first_keys | second_keys
    for key in sorted(keys):
        if key not in data1:
            nodes.append({'key': key, 'type': ADDED, 'value': data2[key]})
        elif key not in data2:
            nodes.append({'key':key, 'type': DELETED, 'value': data1[key]})
        elif data1.get(key) == data2.get(key):
            nodes.append({'key': key, 'type': UNCHANGED, 'value': data1[key]})
        elif isinstance(
            data1.get(key), dict) and isinstance(
                data2.get(key), dict):
            nodes.append({'key': key, 'type': NESTED, 'value': build_diff(
                data1.get(key), data2.get(key))})
        else:
            nodes.append({'key':key, 'type':CHANGED, 'value': (data1[key], data2[key])})
    return nodes

# def build_diff(data1, data2):
#     nodes = {}
#     added_keys = data2.keys() - data1.keys()
#     deleted_keys = data1.keys() - data2.keys()
#     intersection_keys = data1.keys() & data2.keys()
#     for key in added_keys:
#         nodes[key] = [ADDED, data2[key]]
#     for key in deleted_keys:
#         nodes[key] = [DELETED, data1[key]]
#     for key in intersection_keys:
#         nodes[key] = create_intersection_diff(
#             data1[key], data2[key])
#     return nodes


# def create_intersection_diff(data1, data2):
#     if isinstance(data1, dict) and isinstance(data2, dict):
#         return [NESTED, build_diff(data1, data2)]
#     if data1 == data2:
#         return [UNCHANGED, data1]
#     return [CHANGED, data1, data2]
# def make_entry(data1, data2, value):
#     node_dict = {
#         'type': value,
#         'key': value,
#         'first_value': value,
#         'second_value': value,
#     }
#     if node_dict['type'] == ADDED:
#         return node_dict.update({'second_value': data2['key']})
#     elif node_dict['type'] == DELETED:
#         return node_dict.update({'first_value': data1['key']})
#     elif node_dict['type'] == UNCHANGED:
#         return node_dict.update({'first_value': data1['key']})
#     # elif node_dict['type'] == CHANGED:
#     #     value = ({'first_value': data1['key'], 'second_value': data2['key']})
#         return node_dict.update(value)
#     else: value = build_diff(data1['key'], data2['key'])


# def build_diff(data1, data2):
#     nodes = []
#     first_keys = data1.keys()
#     second_keys = data2.keys()
#     keys = first_keys | second_keys
#     for key in sorted(keys):
#         if key not in data1:
#             nodes.append(make_entry(data1, data2, ADDED))
#         # elif key not in data2:
#         #     nodes.append(make_entry(data1, data2, DELETED))
#         elif data1.get(key) == data2.get(key):
#             nodes.append(make_entry(data1, data2, UNCHANGED))
#         elif isinstance(
#             data1.get(key), dict) and isinstance(
#                 data2.get(key), dict):
#             nodes.append(make_entry(data1, data2, NESTED))
#         else:
#             nodes.append(make_entry(data1, data2, CHANGED))
#     return nodes

# def make_entry(data1, data2, value, key):
#     node_dict = {
#         'type': value,
#         'key': value,
#         'first_value': value,
#         'second_value': value,
#         'nested': value
#     }
#     if node_dict['type'] == ADDED:
#         return node_dict.update({'second_value': data2[key]})
    

# def build_diff(data1, data2):
#     nodes = []
#     first_keys = data1.keys()
#     second_keys = data2.keys()
#     keys = first_keys | second_keys
#     for key in sorted(keys):
#         if key not in data1:
#             nodes.append({'type': ADDED, 'key': key, 'second_value': data2[key]})
#         elif key not in data2:
#             nodes.append({'type': DELETED,'key':key, 'first_value': data1[key]})
#         elif data1.get(key) == data2.get(key):
#             nodes.append({'type': UNCHANGED, 'key': key, 'first_value': data1[key]})
#         elif isinstance(
#             data1.get(key), dict) and isinstance(
#                 data2.get(key), dict):
#             nodes.append({'type': NESTED, 'key': key, NESTED: build_diff(
#                 data1.get(key), data2.get(key))})
#         else:
#             nodes.append({'type':CHANGED, 'key':key, 'first_value': data1[key], 'second_value': data2[key]})
#     return nodes


# def build_diff(data1, data2):
#     nodes = []
#     first_keys = data1.keys()
#     second_keys = data2.keys()
#     keys = first_keys | second_keys
#     for key in sorted(keys):
#         if key not in data1:
#             nodes.append({'type': ADDED, 'key': key, 'second_value': data2[key]})
#         elif key not in data2:
#             nodes.append({'type': DELETED,'key':key, 'first_value': data1[key]})
#         elif data1.get(key) == data2.get(key):
#             nodes.append({'type': UNCHANGED, 'key': key, 'first_value': data1[key]})
#         elif isinstance(
#             data1.get(key), dict) and isinstance(
#                 data2.get(key), dict):
#             nodes.append({'type': NESTED, 'key': key, NESTED: build_diff(
#                 data1.get(key), data2.get(key))})
#         else:
#             nodes.append({'type':CHANGED, 'key':key, 'first_value': data1[key], 'second_value': data2[key]})
#     print(nodes)
#     return nodes


# def build_diff(data1, data2):
#     first_keys = data1.keys()
#     second_keys = data2.keys()
#     keys = first_keys | second_keys
#     nodes = []

#     for key in sorted(keys):
#         if key not in data1:
#             ast = {'type': ADDED, 'key': key,
#                    'second_value': data2.get(key)
#                    }
#         elif key not in data2:
#             ast = {'type': DELETED, 'key': key,
#                    'first_value': data1.get(key)
#                    }
#         elif data1.get(key) == data2.get(key):
#             ast = {'type': UNCHANGED, 'key': key,
#                    'first_value': data1.get(key)
#                    }
#         elif isinstance(
#             data1.get(key), dict) and isinstance(
#                 data2.get(key), dict):
#             ast = {'type': NESTED, 'key': key,
#                    'nested': build_diff(data1.get(key),
#                                         data2.get(key))}
#         else:
#             ast = {'type': CHANGED, 'key': key,
#                    'first_value': data1.get(key),
#                    'second_value': data2.get(key)
#                    }
#         nodes.append(ast)
#     return nodes
