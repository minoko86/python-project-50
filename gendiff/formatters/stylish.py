from gendiff.tree import is_updated


def stringify(lst, inset=0):
    result = '{\n'
    spacing = inset * 4 * ' '
    for item in lst:
        result = result + spacing + string_of_item(item, inset)
    result = result + spacing + '}'
    return result


def string_of_item(item, inset):
    if is_updated(item):
        _, k, v1, v2 = item
        v1 = get_value_string(v1, inset)
        v2 = get_value_string(v2, inset)
        spacing = inset * 4 * ' '
        return f'  - {k}: {v1}\n {spacing} + {k}: {v2}\n'
    else:
        s, k, v = item
        v = get_value_string(v, inset)
        return f'  {s} {k}: {v}\n'


def get_value_string(value, inset=0):
    if isinstance(value, list):
        return stringify(value, inset + 1)
    if isinstance(value, bool):
        if value:
            return 'true'
        return 'false'
    return value
