from gendiff.generator import generate_diff
import tests.expected as expected


def test1_simple_stylish():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'stylish')
    assert actual == expected.SIMPLE_STYLISH


def test2_simple_plain():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'plain')
    assert actual == expected.SIMPLE_PLAIN


def test3_simple_json():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'json')
    assert actual == expected.SIMPLE_JSON


def test4_complex_stylish():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'stylish')
    assert actual == expected.COMPLEX_STYLISH


def test5_complex_plain():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'plain')
    assert actual == expected.COMPLEX_PLAIN


def test6_complex_json():
    actual = generate_diff('./tests/fixtures/complex_before.yaml',
                           './tests/fixtures/complex_after.yaml',
                           'json')
    assert actual == expected.COMPLEX_JSON
