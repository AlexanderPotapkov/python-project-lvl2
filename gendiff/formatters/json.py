import json


def render(ast):
    return json.dumps(ast, indent=2)
