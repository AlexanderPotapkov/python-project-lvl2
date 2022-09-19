from gendiff.formaters.plain import format_value

FILEPATH_JSON1 = 'tests/fixtures/complex_1.json'
FILEPATH_JSON2 = 'tests/fixtures/complex_2.json'
FILEPATH_YAML1 = 'tests/fixtures/complex_1.yaml'
FILEPATH_YAML2 = 'tests/fixtures/complex_2.yaml'


def test_decoding_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value({'a': 'b'}) == '[complex value]'
    assert format_value(300) == 300
