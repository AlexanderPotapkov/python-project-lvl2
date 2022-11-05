import json

def format_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif type(value) == int:
        return value
    else:
        return f"'{value}'"


def format_plain(diff, path=''):
    """Returns formatted difference between two files if plain format
    arguments:
    diff: raw difference between two files
    path: path to value (default: '') using to build full path
    """
    keys = sorted(diff.keys())
    difference = []
    for key in keys:
        status = diff[key]['type']
        full_path = path
        string = get_formatted_object(key, diff, full_path, status)
        if string:
            difference.append(string)
    return '\n'.join(difference)


def get_formatted_object(key, diff, full_path, type):
    """
    Make string in depending of value's type
    arguments:
    key: current key in diff
    diff: part of full difference (value)
    full_path: full path to value
    status: status of value in diff
    """
    if type == 'not changed':
        string = ''

    elif type == 'nested':
        full_path += (f'{key}.')
        string = format_plain(diff[key]['children'], full_path)

    elif type == 'removed':
        full_path += (f'{key}')
        string = (f"Property '{full_path}' was removed")

    elif type == 'added':
        full_path += (f'{key}')
        string = (f"Property '{full_path}' "
                  f"was added with value: {format_value(diff[key]['value'])}")

    elif type == 'updated':
        full_path += (f'{key}')
        string = (f"Property '{full_path}' was updated. "
                  f"From {format_value(diff[key]['value1'])} "
                  f"to {format_value(diff[key]['value2'])}")
    return string
