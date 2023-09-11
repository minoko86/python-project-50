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
            nodes.append({'key': key, 'type': DELETED, 'value': data1[key]})
        elif data1.get(key) == data2.get(key):
            nodes.append({'key': key, 'type': UNCHANGED, 'value': data1[key]})
        elif isinstance(
            data1.get(key), dict) and isinstance(
                data2.get(key), dict):
            nodes.append({'key': key, 'type': NESTED, 'value': build_diff(
                data1[key], data2[key])})
        else:
            nodes.append({'key': key, 'type': CHANGED,
                          'value': (data1[key], data2[key])})
    return nodes
