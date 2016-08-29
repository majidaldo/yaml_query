"""
handles sql stuff in sqlite3
"""

# lots of generators to keep with the spirit of sqlite

import sqlite3


def get_conn(db=':memory:'):
    return sqlite3.connect(db)


def create_table(conn, name, columns):
    c=conn.cursor()
    cols = ', '.join('"{}"'.format(col) for col in columns)
    sql ='create table '+name+' '
    sql+='('+cols+')'
    c.execute(sql)
    conn.commit()
    return c


def insert_into(conn, table_name, values):
    """ insert list of lists of values """
    c=conn.cursor()
    sql= "INSERT INTO "+table_name+" VALUES "
    ncols=len(get_column_names(conn,table_name))
    sql+=str(tuple([0]*ncols)).replace(str(0),'?')# makes (?,?,...,?)
    c.executemany(sql,values)
    conn.commit()
    return c


def list_tables(conn):
    sql='select name from sqlite_master where type=\'table\''
    c=conn.cursor().execute(sql)
    for atbl in c:
        if atbl is None: raise StopIteration #why does it need to give None?!
        else: yield atbl[0]


def get_column_names(conn, table_name):
    c = conn.cursor()
    c.execute("select * from "+table_name)
    return [ member[0] for member in c.description ]
    # c.description wasn't a generator so i didn't use yield


def sql(conn, query):
    conn.row_factory = sqlite3.Row
    c=conn.cursor()
    c.execute(query)
    for arow in c: yield arow

