import json


def get_encoded_bools(first_file, second_file):
    for key in first_file:
        if type(first_file[key]) == bool:
            first_file[key] = json.dumps(first_file[key])
    for key in second_file:
        if type(second_file[key]) == bool:
            second_file[key] = json.dumps(second_file[key])


def generate_diff(file_path_1, file_path_2):
    first_file = json.load(open(file_path_1))
    second_file = json.load(open(file_path_2))
    get_encoded_bools(first_file, second_file)
    only_in_first_file = first_file.keys() - second_file.keys()
    only_in_second_file = second_file.keys() - first_file.keys()
    in_both_files = first_file.keys() & second_file.keys()
    difference = []
    for key in only_in_first_file:
        difference.append(f'  - {key}: {first_file[key]}')
    for key in only_in_second_file:
        difference.append(f'  + {key}: {second_file[key]}')
    for key in in_both_files:
        if first_file[key] == second_file[key]:
            difference.append(f'    {key}: {first_file[key]}')
        else:
            difference.append(f'  - {key}: {first_file[key]}')
            difference.append(f'  + {key}: {second_file[key]}')
    sorted_difference = sorted(difference, key=lambda x: x[4])
    result = '{\n' + '\n'.join(sorted_difference) + '\n}'
    return result
