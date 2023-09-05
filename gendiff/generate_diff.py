from gendiff.tree import build_diff
from gendiff.parser import load_file
from gendiff.formatters import get_formatter


def generate_diff(file_path1, file_path2, formater_name='stylish'):

    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = build_diff(data1, data2)
    selected_format = get_formatter(formater_name)

    return selected_format(diff)
