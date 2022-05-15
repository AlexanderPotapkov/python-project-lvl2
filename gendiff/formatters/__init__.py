from gendiff.formatters import json, plain, stylish

available_formatters = {
    'json': json.render,
    'plain': plain.render,
    'stylish': stylish.render,
}