from gendiff.generate_difference import generate_diff

JSON_1 = 'tests/fixtures/file_1.json'
JSON_2 = 'tests/fixtures/file_2.json'


def test_generate_diff():
    correct_answer = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff(JSON_1, JSON_2) == correct_answer