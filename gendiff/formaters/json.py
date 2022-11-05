import json


def format_json(diff):
    """Returns formatted difference between two files if json format

    arguments:
    diff: raw difference between two files"""

    return json.dumps(diff)
