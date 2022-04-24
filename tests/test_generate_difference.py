import pytest
from gendiff.generate_difference import generate_diff

JSON_1 = 'tests/fixtures/file_1.json'
JSON_2 = 'tests/fixtures/file_2.json'
JSON_2_1 = 'tests/fixtures/file_2_1.json'
JSON_2_2 = 'tests/fixtures/file_2_2.json'
YAML = 'tests/fixtures/file_2.yaml'
YAML_2_1 = 'tests/fixtures/file_2_1.yaml'
YAML_2_2 = 'tests/fixtures/file_2_2.yaml'
WRONG_FILEPATH = 'tests/fixtures/expectation_json.txt'
EXPECTATION_STYLISH = 'tests/fixtures/expectation_stylish.txt'
EXPECTATION_PLAIN = 'tests/fixtures/expectation_plain.txt'
EXPECTATION_JSON = 'tests/fixtures/expectation_json.txt'


def test_wrong_file_gendiff():
    with pytest.raises(TypeError) as err:
        generate_diff(WRONG_FILEPATH, WRONG_FILEPATH)

    assert str(err.value) == 'Wrong extension!'


def test_wrong_format_gendiff():
    with pytest.raises(TypeError) as err:
        generate_diff(JSON_2_1, JSON_2_2, 'unstylish')

    assert str(err. value) == 'Wrong format!'


def test_default_format():
    assert (generate_diff(JSON_1,
                          JSON_2) == generate_diff(
            JSON_1, JSON_2, 'stylish'))


@pytest.mark.parametrize('first_file, second_file, format, expected', [
    (JSON_2_1, JSON_2_2,
     'stylish', open(EXPECTATION_STYLISH, 'r').read()),
    (JSON_2_1, JSON_2_2,
     'plain', open(EXPECTATION_PLAIN, 'r').read()),
    (JSON_2_1, JSON_2_2,
     'json', open(EXPECTATION_JSON, 'r').read()),
    (YAML_2_1, YAML_2_2,
     'stylish', open(EXPECTATION_STYLISH, 'r').read()),
    (YAML_2_1, YAML_2_2,
     'plain', open(EXPECTATION_PLAIN, 'r').read()),
    (YAML_2_1, YAML_2_2,
     'json', open(EXPECTATION_JSON, 'r').read()), ])
def test_generate_diff(first_file, second_file, format, expected):
    assert generate_diff(first_file, second_file, format) == expected