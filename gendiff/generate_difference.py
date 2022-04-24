import pathlib

from gendiff.formaters import select_formater
from gendiff.parser import get_dict
from gendiff.search_difference import search_difference


def generate_diff(file_path_1, file_path_2, format='stylish'):
    dict_1 = get_dict(get_string(file_path_1),
                      pathlib.PurePosixPath(file_path_1).suffix)
    dict_2 = get_dict(get_string(file_path_2),
                      pathlib.PurePosixPath(file_path_1).suffix)

    difference = search_difference(dict_1, dict_2)

    return select_formater(format)(difference)


def get_string(file_path):
    with open(file_path, 'r') as file_object:
        string = file_object.read()
    return string
