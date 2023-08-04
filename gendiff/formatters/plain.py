from gendiff.tree import is_updated
from gendiff.tree import is_added
from gendiff.tree import is_removed
from gendiff.tree import get_key
from gendiff.tree import get_value


def stringify(lst):
    result = []
    for item in lst:
        result.extend(strings_of_item(item))
    return '\n'.join(result)


def strings_of_item(item, parent_key=''):  # noqa: C901
    key = get_key(item)
    if len(parent_key) > 0:
        key = parent_key + '.' + key
    value = get_value(item)
    if is_added(item):
        value = get_value_string(value)
        return [f'Property \'{key}\' was added with value: {value}']
    if is_removed(item):
        return [f'Property \'{key}\' was removed']
    if is_updated(item):
        value1 = (get_value_string(value[0]))
        value2 = (get_value_string(value[1]))
        return [f'Property \'{key}\' was updated. From {value1} to {value2}']
    if isinstance(value, list):
        result = []
        for child in value:
            result.extend(strings_of_item(child, key))
        return result
    return []


def get_value_string(value):
    if value == 'null':
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return '[complex value]'
    return f'\'{value}\''
