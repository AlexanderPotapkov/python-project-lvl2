from gendiff.search_difference import (
    get_keys,
    is_dictionary,
    search_difference,
    get_value
)


def test_is_dictionary():
    assert is_dictionary({"key": "value", "not_key": "not_value"}) is True
    assert is_dictionary("100_percent_dictionary") is False


def test_get_keys():
    dict_1 = {"a": "aa", "b": "bb"}
    dict_2 = {"b": "bb", "c": "cc"}
    assert get_keys(dict_1, dict_2) == {"a", "b", "c"}


def test_search_difference():
    dict_1 = {"a": "aa", "b": "bb", "d": {"dd": "ddd"}}
    dict_2 = {"b": "bbb", "c": "cc", "d": {"dd": "dddd"}}
    expectation = (
    {'a': {'status': 'removed', 'value': 'aa'},  # noqa
     'b': {'status': 'updated', 'value1': 'bb',
           'value2': 'bbb'},
     'c': {'status': 'added', 'value': 'cc'},
     'd': {'status': 'nested', 'children':
           {'dd': {'status': 'updated',
                   'value1': 'ddd', 'value2': 'dddd'}}}
     })
    assert search_difference(dict_1, dict_2) == expectation


def test_get_value():
    dict_1 = {"a": "aa", "b": "bb"}
    dict_2 = {"b": "bb", "c": "cc"}
    assert get_value(dict_1, dict_2, 'a') == {
        'status': 'removed',
        'value': 'aa'}
    assert get_value(dict_1, dict_2, 'b') == {
        'status': 'not changed',
        'value': 'bb'}
    assert get_value(dict_1, dict_2, 'c') == {
        'status': 'added',
        'value': 'cc'}