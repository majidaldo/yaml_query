# yaml_query
Use a YAML file as a table to query.

## Quick Start

Suppose you have a YAML file that describes items as follows. You'd like to 'filter' the items for certain attributes.

```
---

#item_column: ITEM_ID # special

test:
  test: 123

item1:
  field1: asdf
  field2: 123
  cool: tag # get the 'tag' effect

item2:
  field1: asdf2
  field2: 123
  hot: tag
  any: 1
  number: 2
  of: 3
  fields: 4


specialone:
  myfield: is unique
  date_type: 2011-11-11
  float_type: 1.2
  bool_type: True
```

Use SQL to `yaml_query` items in the file as follows:

`python -m yaml_query.yaml_query 'select ITEM_ID from file.yaml where field2=123'`

Result
```
"item2",
"item1",
```
