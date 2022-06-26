"""investment db module"""

#!/usr/bin/python3

import pandas as pd
import sqlalchemy as sql

USER = 'fmg'
PW = 'fmg'
HOST = '127.0.0.1'
DB = 'fmg'

CONNECTION_STRING = 'mysql+pymysql://'+USER+':'+PW+'@'+HOST+'/'+DB+''
sql_engine = sql.create_engine(CONNECTION_STRING)

def get_mysql_data(table:str):
    """
    Receive the complete table as dataframe.

    Parameters
    ----------
    table : str

    Returns
    -------
    panda.DataFrame
    """
    query = "SELECT * FROM " + table
    return pd.read_sql_query(query, sql_engine)

def put_dict_to_mysql(table:str, data:dict):
    """
    Write dict to table with keys = columns, values = values.

    Parameters
    ----------
    table : str
    data : dict

    Returns
    -------
    None
    """
    columns = "`%s`" % '`, `'.join(data.keys())    # string build on column names
    placeholders = ', '.join(['%s'] * len(data))  # string build %s based on number of colums
    on_duplicate = "`%s`" % '` = %s, `'.join(data.keys())    # string build on column names
    on_duplicate = on_duplicate + ' = %s'
    sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON DUPLICATE KEY UPDATE %s;" % (table, columns, placeholders, on_duplicate)
    sql_engine.execute(sql, list(data.values()) + list(data.values()))

def get_financial_statement():
    """
    Receive the complete financials list as dataframe.

    Parameters
    ----------
    none

    Returns
    -------
    panda.DataFrame
    """
    return get_mysql_data('financials')

def put_financial_statement(symbol:str):
    """
    Put a 'symbol' to the database.

    Parameters
    ----------
    symbol : str

    Returns
    -------
    None
    """
    query = "INSERT INTO "+'financials'+" (`symbol`, `checked`) VALUES ('"+symbol+"', NOW()) ON DUPLICATE KEY UPDATE checked = NOW();"
    sql_engine.execute(query)
    return 0

# ---

def get_symbols_list_overview():
    query = "SELECT symbol FROM symbolslist ORDER BY `checked` ASC"
    return pd.read_sql_query(query, sql_engine)

def put_symbols_list(data:dict):
    put_dict_to_mysql('symbolslist', data)

def put_symbols_list_checked(symbol:str):
    query = "UPDATE "+'symbolslist'+" SET `checked` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

def put_symbols_list_updated(symbol:str):
    query = "UPDATE "+'symbolslist'+" SET `updated` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

# ---

def get_company_key_stats_overview():
    query = "SELECT symbol FROM companykeystats ORDER BY `checked` ASC"
    return pd.read_sql_query(query, sql_engine)

def get_company_key_stats_currencies():
    query = "SELECT `currency`, count(*) as `count` FROM fmg.companykeystats WHERE length(`currency`) = 3 GROUP BY `currency` ORDER BY `count` DESC;"
    return pd.read_sql_query(query, sql_engine)


def put_company_key_stats(data:dict):
    put_dict_to_mysql('companykeystats', data)

def put_company_key_stats_checked(symbol:str):
    query = "UPDATE "+'companykeystats'+" SET `checked` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

def put_company_key_stats_updated(symbol:str):
    query = "UPDATE "+'companykeystats'+" SET `updated` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

# ---

def put_dict_list_to_table(data:dict, table:str):
    put_dict_to_mysql(table, data)

def put_symbol_checked(symbol:str, table:str, **kwargs):
    date = kwargs.get('date', None)
    if date:
        query = "UPDATE "+table+" SET `checked` = NOW() WHERE `symbol` = '"+symbol+"' AND `date` = '"+date+"';"
    else:
        query = "UPDATE "+table+" SET `checked` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

def put_symbol_updated(symbol:str, table:str, **kwargs):
    date = kwargs.get('date', None)
    if date:
        query = "UPDATE "+table+" SET `updated` = NOW() WHERE `symbol` = '"+symbol+"' AND `date` = '"+date+"';"
    else:
        query = "UPDATE "+table+" SET `updated` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)
