from gendiff.tree import build_diff
from gendiff.parser import parse
from gendiff.formatters import formatting


def generate_diff(file_path1, file_path2, formater_name='stylish'):

    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff = build_diff(data1, data2)
    selected_format = formatting(formater_name)

    return selected_format(diff)
