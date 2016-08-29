from __future__ import print_function

"""
'query' the YAML file (as a named entity in on the f/s).
stuff here is just for convenience.

"""

import os
from . import dict2table
from . import sql as _sql
from . import yaml2sql



def _get_files_in_sql(sql_query):
    """ get yaml file in sql """
    files = []
    for aword in sql_query.split(' '):
        if os.path.isfile(aword):
            files.append(aword)
    return files

def _replace_yamlfiles_in_sql(sql_query):
    """ replace file pathing in sql """
    # file.yaml is valid is sqlite but removing them in ext

    for afile in _get_files_in_sql(sql_query):
        table_name = yaml2sql.get_table_name(afile)
        sql_query = sql_query.replace(afile,table_name)
    return sql_query


def sql(conn,query):
    query = _replace_yamlfiles_in_sql(query)
    return _sql.sql(conn,query)


def select_items(conn,query):
    # eh not really needed b/c you can just select ITEM_ID
    # todo: remove
    """ returns just the items (IDs) in query """
    for arow in sql(conn,query):
        yield arow[dict2table.item_column]


def query_yamlfiles(sql_query):
    """ Just a convenience b/c it creates the db connection within."""
    yf = _get_files_in_sql(sql_query)
    if len(yf)==0:
        raise ValueError('no yaml files in sql query')

    conn = yaml2sql.yaml2sql(yf[0]) # make the first table
    for ayf in yf[1:]: # insert the others
        yaml2sql.yaml2sql(ayf, connection=conn)

    items = sql(conn,sql_query)
    return items


if __name__=='__main__':
    
    import sys
    sql_query = sys.argv[1]

    items = query_yamlfiles(sql_query)

    for anitem in items:
        toprint = anitem
        toprint = [ '"'+str(acol).replace('"','\\"')+'",'
                            for acol in toprint]
        print(*toprint)


# todo: the abstraction should be 'named' dictionaries
# it just happens that the dictionary names are files
# but they'd only have 'names' if they came from storage anyways right??
