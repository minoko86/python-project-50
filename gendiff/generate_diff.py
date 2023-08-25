from gendiff.tree import build_diff
from gendiff.parser import parse
from gendiff.formatters import formatting


def generate_diff(file_path1, file_path2, formater_name='stylish'):
    # first_data, first_format = read_file(file_path1)
    # second_data, second_format = read_file(file_path2)

    # data1 = parse(first_data, first_format)
    # data2 = parse(second_data, second_format)

    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff = build_diff(data1, data2)
    selected_format = formatting(formater_name)

    return selected_format(diff)


# def read_file(file_name):

#     with open(file_name, 'r') as file:
#         file_data = file.read()
#         fyle_format = file_name.split('.')[-1]
#         return file_data, fyle_format
