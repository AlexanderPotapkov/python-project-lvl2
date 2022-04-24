from gendiff.formaters.plain import format_value

JSON_1 = 'tests/fixtures/file_2_1.json'
JSON_2 = 'tests/fixtures/file_2_2.json'
YAML_1 = 'tests/fixtures/file_2_1.yaml'
YAML_2 = 'tests/fixtures/file_2_2.yaml'


def test_decoding_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value({'a': 'b'}) == '[complex value]'
    assert format_value(300) == 300