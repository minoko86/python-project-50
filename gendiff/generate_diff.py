import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.json as jsonin
from gendiff.tree import generate_diff_tree


def generate_diff(file_path1, file_path2, formater_name='stylish'):
    diff_tree = generate_diff_tree(file_path1, file_path2)
    formater = stylish
    if formater_name == 'plain':
        formater = plain
    elif formater_name == 'json':
        formater = jsonin
    return formater.stringify(diff_tree)
