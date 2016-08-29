"""
handles nested (1-level) dictionary data (like in the yaml file).
"""


item_column = 'ITEM_ID' # special


def iter_rows(item_dict,columns):
    """
    Iterate through the {'item':{'attrib':'value'}} items as rows in a table.
    Values for items with no 'keys' in columns will be blank.
    """
    d = item_dict
    for item in d:
        d[item][item_column]=item 
        values =  [
            d[item][acol]
            if acol in d[item]
            else None #''?
            for acol in columns
        ]
        yield values


def dict2table(*args,**kwargs):
    return iter_rows(*args,**kwargs)

def get_fields(item_dict):
    d = item_dict
    fields=set()
    for item in d:
        for afield in d[item]:
            fields.add(afield)
    return fields
