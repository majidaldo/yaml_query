import yaml2dict
import sql
import dict2table

import os


def get_table_name(yaml_path):
    """gives how the yaml file name should be in the sql query"""
    table_name = os.path.basename(yaml_path)
    table_name = os.path.splitext(table_name)[0]
    return table_name

def yaml2sql(yaml_path, connection=None):
    """
    just point to a yaml file
    and you'll get back a db connection to query
    the file name w/o the extention or path will be used as the table name
    """
    fp=yaml_path;
    conn = connection
    if conn is None: conn=sql.get_conn()

    yd=yaml2dict.yaml2dict(open(fp));
    
    table_name = get_table_name(yaml_path)
    if table_name in sql.list_tables(conn):
        ValueError('table '+yaml_path+' already in db')

    columns= dict2table.get_fields(yd)
    columns=[dict2table.item_column]+list(columns)
    sql.create_table(conn,table_name,columns)

    ir =  dict2table.iter_rows(yd,columns); 
    sql.insert_into(conn,table_name,ir)

    return conn
