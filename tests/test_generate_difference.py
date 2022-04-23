import pytest
from gendiff.generate_difference import generate_diff

@pytest.fixture
def json_path_1():
    return 'tests/fixtures/file_1.json'


@pytest.fixture
def json_path_2():
    return 'tests/fixtures/file_2.json'


def test_json(json_path_1, json_path_2):
    excepted = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(json_path_1, json_path_2) == excepted


@pytest.fixture
def yaml_path_1():
    return 'tests/fixtures/file_1.yaml'


@pytest.fixture
def yaml_path_2():
    return 'tests/fixtures/file_2.yaml'


def test_yaml(yaml_path_1, yaml_path_2):
    excepted = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(yaml_path_1, yaml_path_2) == excepted