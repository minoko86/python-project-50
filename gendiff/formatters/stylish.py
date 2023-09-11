import json

from gendiff.tree import DELETED, ADDED, NESTED, UNCHANGED


NEW = '+'
OLD = '-'
NOCHANGE = ' '
NUMBER_OF_SPACES = 4
SPACE = ' '
TEMPLATE_STYLISH = '{0}{1} {2}: {3}'


def make_format(node, depth=1):
    output = ['{']
    start_space = get_space(depth).get('start')
    end_space = get_space(depth).get('end')

    for item in node:
        if item['type'] is DELETED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, OLD, item['key'],
                get_string(item['value'], depth + 1)
            ))
        elif item['type'] is ADDED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, NEW, item['key'],
                get_string(item['value'], depth + 1)
            ))
        elif item['type'] is UNCHANGED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, NOCHANGE, item['key'],
                get_string(item['value'], depth + 1)
            ))
        elif item['type'] is NESTED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, NOCHANGE, item['key'],
                make_format(item['value'], depth + 1)
            ))
        else:
            output.append(TEMPLATE_STYLISH.format(
                start_space, OLD, item['key'],
                get_string(item['value'][0], depth + 1)
            ))
            output.append(TEMPLATE_STYLISH.format(
                start_space, NEW, item['key'],
                get_string(item['value'][1], depth + 1)
            ))

    output.append(end_space + '}')
    return '\n'.join(output)


def get_space(depth):
    space = {'start': SPACE * (NUMBER_OF_SPACES * depth - 2),
             'end': SPACE * (NUMBER_OF_SPACES * (depth - 1))}
    return space


def get_string(value, depth):
    result = []
    start_space = get_space(depth).get('start')
    end_space = get_space(depth).get('end')

    if isinstance(value, dict):
        result.append('{')
        for key, leaf_value in value.items():
            result.append(TEMPLATE_STYLISH.format(
                start_space, NOCHANGE,
                key, get_string(leaf_value, depth + 1)
            ))

        result.append(end_space + '}')
    elif isinstance(value, str):
        result.append(value)
    else:
        result.append(json.dumps(value))
    return '\n'.join(result)
