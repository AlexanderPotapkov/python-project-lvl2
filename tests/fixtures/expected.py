# -*- coding: utf-8 -*-

SIMPLE_STYLISH = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

COMPLEX_STYLISH = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

SIMPLE_PLAIN = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

COMPLEX_PLAIN = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

SIMPLE_JSON = """{"follow": {"status": "removed", "value": false}, "host": {"status": "not changed", "value": "hexlet.io"}, "proxy": {"status": "removed", "value": "123.234.53.22"}, "timeout": {"status": "updated", "value1": 50, "value2": 20}, "verbose": {"status": "added", "value": true}}"""

COMPLEX_JSON = """{"common": {"status": "nested", "children": {"follow": {"status": "added", "value": false}, "setting1": {"status": "not changed", "value": "Value 1"}, "setting2": {"status": "removed", "value": 200}, "setting3": {"status": "updated", "value1": true, "value2": null}, "setting4": {"status": "added", "value": "blah blah"}, "setting5": {"status": "added", "value": {"key5": "value5"}}, "setting6": {"status": "nested", "children": {"doge": {"status": "nested", "children": {"wow": {"status": "updated", "value1": "", "value2": "so much"}}}, "key": {"status": "not changed", "value": "value"}, "ops": {"status": "added", "value": "vops"}}}}}, "group1": {"status": "nested", "children": {"baz": {"status": "updated", "value1": "bas", "value2": "bars"}, "foo": {"status": "not changed", "value": "bar"}, "nest": {"status": "updated", "value1": {"key": "value"}, "value2": "str"}}}, "group2": {"status": "removed", "value": {"abc": 12345, "deep": {"id": 45}}}, "group3": {"status": "added", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}}"""