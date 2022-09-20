import pytest
from gendiff.generate_difference import generate_diff
from tests.fixtures.expected import (SIMPLE_STYLISH,
                                     SIMPLE_PLAIN,
                                     SIMPLE_JSON,
                                     COMPLEX_STYLISH,
                                     COMPLEX_PLAIN,
                                     COMPLEX_JSON)

FILEPATH_JSON_1_1 = 'tests/fixtures/simple_1.json'
FILEPATH_JSON_1_2 = 'tests/fixtures/simple_2.json'
FILEPATH_JSON_2_1 = 'tests/fixtures/complex_1.json'
FILEPATH_JSON_2_2 = 'tests/fixtures/complex_2.json'
FILEPATH_YAML_1_1 = 'tests/fixtures/simple_1.yaml'
FILEPATH_YAML_1_2 = 'tests/fixtures/simple_2.yaml'
FILEPATH_YAML_2_1 = 'tests/fixtures/complex_1.yaml'
FILEPATH_YAML_2_2 = 'tests/fixtures/complex_2.yaml'
FILEPATH_WRONG = 'tests/fixtures/expectation_json.txt'


def test_wrong_file_gendiff():
    with pytest.raises(TypeError) as err:
        generate_diff(FILEPATH_WRONG, FILEPATH_WRONG)

    assert str(err.value) == 'Wrong extension!'


def test_wrong_format_gendiff():
    with pytest.raises(TypeError) as err:
        generate_diff(FILEPATH_JSON_2_1, FILEPATH_JSON_2_2, 'unstylish')

    assert str(err.value) == 'Wrong format!'


def test_default_format():
    assert (generate_diff(FILEPATH_JSON_1_1,
                          FILEPATH_JSON_1_2) == generate_diff(
        FILEPATH_JSON_1_1, FILEPATH_JSON_1_2, 'stylish'))


@pytest.mark.parametrize('first_file, second_file, format, expected', [
    (FILEPATH_JSON_1_1, FILEPATH_JSON_1_2,
     'stylish', SIMPLE_STYLISH),
    (FILEPATH_JSON_2_1, FILEPATH_JSON_2_2,
     'stylish', COMPLEX_STYLISH),
    (FILEPATH_JSON_1_1, FILEPATH_JSON_1_2,
     'plain', SIMPLE_PLAIN),
    (FILEPATH_JSON_2_1, FILEPATH_JSON_2_2,
     'plain', COMPLEX_PLAIN),
    (FILEPATH_JSON_1_1, FILEPATH_JSON_1_2,
     'json', SIMPLE_JSON),
    (FILEPATH_JSON_2_1, FILEPATH_JSON_2_2,
     'json', COMPLEX_JSON),
    (FILEPATH_YAML_1_1, FILEPATH_YAML_1_2,
     'stylish', SIMPLE_STYLISH),
    (FILEPATH_YAML_2_1, FILEPATH_YAML_2_2,
     'stylish', COMPLEX_STYLISH),
    (FILEPATH_YAML_1_1, FILEPATH_YAML_1_2,
     'plain', SIMPLE_PLAIN),
    (FILEPATH_YAML_2_1, FILEPATH_YAML_2_2,
     'plain', COMPLEX_PLAIN),
    (FILEPATH_YAML_1_1, FILEPATH_YAML_1_2,
     'json', SIMPLE_JSON),
    (FILEPATH_YAML_2_1, FILEPATH_YAML_2_2,
     'json', COMPLEX_JSON,), ])
def test_generate_diff(first_file, second_file, format, expected):
    assert generate_diff(first_file, second_file, format) == expected
