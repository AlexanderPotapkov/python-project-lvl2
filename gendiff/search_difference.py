def search_difference(first_file, second_file):
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
    return difference
