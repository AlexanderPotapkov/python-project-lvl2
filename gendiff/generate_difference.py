import json
import pathlib
import yaml

from gendiff.search_difference import search_difference


def get_encoded_bools(file):
    for key in file:
        if type(file[key]) == bool:
            file[key] = json.dumps(file[key])


def generate_diff(file_path_1, file_path_2):
    file_1_format = pathlib.PurePosixPath(file_path_1).suffix
    file_2_format = pathlib.PurePosixPath(file_path_2).suffix
    if file_1_format == '.json':
        first_file = json.load(open(file_path_1))
    elif file_1_format == '.yml' or file_1_format == '.yaml':
        first_file = yaml.safe_load(open(file_path_1))
    if file_2_format == '.json':
        second_file = json.load(open(file_path_2))
    elif file_2_format == '.yml' or file_2_format == '.yaml':
        second_file = yaml.safe_load(open(file_path_2))
    get_encoded_bools(first_file)
    get_encoded_bools(second_file)
    difference = search_difference(first_file, second_file)
    sorted_difference = sorted(difference, key=lambda x: x[4])
    result = '{\n' + '\n'.join(sorted_difference) + '\n}'
    return result
