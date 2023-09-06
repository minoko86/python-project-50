DELETED = 'deleted'
ADDED = 'added'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
NESTED = 'nested'


def make_entry(type, key, first_value='', second_value=''):
    return {
        'type': type,
        'key': key,
        'first_value': first_value,
        'second_value': second_value,
        # 'nested': nested,
    }


def build_diff(data1, data2):
    nodes = []
    first_keys = data1.keys()
    second_keys = data2.keys()
    keys = first_keys | second_keys
    for key in sorted(keys):
        if key not in data1:
            nodes.append(make_entry(ADDED, key, data2[key]))
        elif key not in data2:
            nodes.append(make_entry(DELETED, key, data1[key]))
        elif data1.get(key) == data2.get(key):
            nodes.append(make_entry(UNCHANGED, key, data1[key]))
        elif isinstance(
            data1.get(key), dict) and isinstance(
                data2.get(key), dict):
            nodes.append(make_entry(NESTED, key, build_diff(
                data1.get(key), data2.get(key))))
        else:
            nodes.append(make_entry(CHANGED, key, data1[key], data2[key]))
    return nodes


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
