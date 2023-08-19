from gendiff.constants import ADDED, REMOVED, NONCHANGED, UPDATED

import json
import yaml


def get_dictionary_from_file(file_path):
    with open(file_path) as o:
        if file_path[-4:] == 'json':
            return json.load(o)
        if file_path[-4:] == 'yaml' or file_path[-3:] == 'yml':
            return yaml.safe_load(o)


def build_added_node(key, value):
    value = get_dict_value(value)
    return (ADDED, key, value)


def build_removed_node(key, value):
    value = get_dict_value(value)
    return (REMOVED, key, value)


def build_nonchanged_node(key, value):
    value = get_dict_value(value)
    return (NONCHANGED, key, value)


def build_updated_node(key, value1, value2):
    value1 = get_dict_value(value1)
    value2 = get_dict_value(value2)
    return (UPDATED, key, value1, value2)


def generate_diff_tree(file_path1, file_path2):
    file1_dict = get_dictionary_from_file(file_path1)
    file2_dict = get_dictionary_from_file(file_path2)
    return get_diff_tree(file1_dict, file2_dict)


def get_diff_tree(dict1, dict2):
    dict1 = cut_null_values(dict1)
    dict2 = cut_null_values(dict2)
    result = []
    for key in get_keys(dict1, dict2):
        diff_strings = get_diff_child_tree(
            key, dict1.get(key), dict2.get(key))
        result.extend(diff_strings)
    return result


def cut_null_values(dictionary):
    result = {}
    for k, v in dictionary.items():
        if v is None:
            v = 'null'
        result[k] = v
    return result


def get_keys(dict1, dict2):
    keyset = set()
    keyset.update(dict1.keys())
    keyset.update(dict2.keys())
    keylist = list(keyset)
    keylist.sort()
    return keylist


def get_diff_child_tree(key, value1, value2):
    if value1 is None:
        return [build_added_node(key, value2)]
    if value2 is None:
        return [build_removed_node(key, value1)]
    if value1 == value2:
        return [build_nonchanged_node(key, value1)]
    if isinstance(value1, dict) and isinstance(value2, dict):
        return [build_nonchanged_node(
            key, get_diff_tree(value1, value2))]
    return [build_updated_node(key, value1, value2)]


def is_added(node):
    return node[0] == ADDED


def is_removed(node):
    return node[0] == REMOVED


def is_non_changed(node):
    return node[0] == NONCHANGED


def is_updated(node):
    return node[0] == UPDATED


def get_key(node):
    return node[1]


def get_value(node):
    if len(node) == 4:
        return (node[2], node[3])
    return node[2]


def get_dict_value(value):
    if isinstance(value, dict):
        result = []
        for k, v in value.items():
            result.append(build_nonchanged_node(k, v))
        return result
    return value
