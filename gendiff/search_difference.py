def is_dictionary(object):
    return isinstance(object, dict)


def get_keys(dict_1, dict_2):
    return set(list(dict_1.keys()) + list(dict_2.keys()))


def search_difference(dict_1, dict_2):
    keys = sorted(get_keys(dict_1, dict_2))
    difference = {}
    for key in keys:
        difference[key] = get_value(dict_1, dict_2, key)
    return difference


def get_value(dict_1, dict_2, key):
    if key in dict_1 and key not in dict_2:
        value = {
            'status': 'removed',
            'value': dict_1.get(key)}
    elif key in dict_2 and key not in dict_1:
        value = {
            'status': 'added',
            'value': dict_2.get(key)}
    elif dict_1[key] == dict_2[key]:
        value = {
            'status': 'not changed',
            'value': dict_1.get(key)}
    elif not is_dictionary(dict_1[key]) or not is_dictionary(dict_2[key]):
        value = {
            'status': 'updated',
            'value1': dict_1.get(key),
            'value2': dict_2.get(key)}
    elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
        value = {
            'status': 'nested',
            'children': search_difference(dict_1[key], dict_2[key])}
    return value
