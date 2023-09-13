import json


def make_format(node):
    return json.dumps(node, indent=2)
