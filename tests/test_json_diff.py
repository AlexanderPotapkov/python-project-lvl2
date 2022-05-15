from gendiff.generator import generate_diff
import tests.expected as expected


def test1_simple_stylish():
    actual = generate_diff('./tests/fixtures/simple_before.json',
                           './tests/fixtures/simple_after.json',
                           'stylish')
    assert actual == expected.SIMPLE_STYLISH


def test2_simple_plain():
    actual = generate_diff('./tests/fixtures/simple_before.json',
                           './tests/fixtures/simple_after.json',
                           'plain')
    assert actual == expected.SIMPLE_PLAIN


def test3_simple_json():
    actual = generate_diff('./tests/fixtures/simple_before.json',
                           './tests/fixtures/simple_after.json',
                           'json')
    assert actual == expected.SIMPLE_JSON


def test4_complex_stylish():
    actual = generate_diff('./tests/fixtures/complex_before.json',
                           './tests/fixtures/complex_after.json',
                           'stylish')
    assert actual == expected.COMPLEX_STYLISH


def test5_complex_plain():
    actual = generate_diff('./tests/fixtures/complex_before.json',
                           './tests/fixtures/complex_after.json',
                           'plain')
    assert actual == expected.COMPLEX_PLAIN


def test6_complex_json():
    actual = generate_diff('./tests/fixtures/complex_before.json',
                           './tests/fixtures/complex_after.json',
                           'json')
    assert actual == expected.COMPLEX_JSON
