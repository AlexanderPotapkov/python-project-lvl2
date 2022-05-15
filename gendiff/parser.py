import json
import yaml


def parser(file_data, file_type):
    mapping = {
        '.json': json.loads,
        '.yaml': lambda file_data: yaml.load(file_data, Loader=yaml.SafeLoader),
    }
    return mapping[file_type](file_data)
