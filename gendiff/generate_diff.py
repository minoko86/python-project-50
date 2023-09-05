from gendiff.tree import build_diff
from gendiff.parser import open_the_file
from gendiff.formatters import get_format


def generate_diff(file_path1, file_path2, formater_name='stylish'):

    data1 = open_the_file(file_path1)
    data2 = open_the_file(file_path2)

    diff = build_diff(data1, data2)
    selected_format = get_format(formater_name)

    return selected_format(diff)
