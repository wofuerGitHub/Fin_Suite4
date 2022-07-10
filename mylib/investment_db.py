"""investment db module"""

#!/usr/bin/python3

from datetime import datetime
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

# ---quotes

def get_quote_to_insert():
    query = "SELECT symbol, currency FROM referencedata WHERE longTimeSerie = 1 ORDER BY `updated` ASC"
    return pd.read_sql_query(query, sql_engine)

def set_quote_to_stream_only(symbol:str):
    query = "UPDATE referencedata SET `longTimeSerie` = 0,  `updated`=NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

# ---
def put_company_key_stats(data:dict):
    put_dict_to_mysql('companykeystats', data)

def put_company_key_stats_checked(symbol:str):
    query = "UPDATE "+'companykeystats'+" SET `checked` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

def put_company_key_stats_updated(symbol:str):
    query = "UPDATE "+'companykeystats'+" SET `updated` = NOW() WHERE `symbol` = '"+symbol+"';"
    sql_engine.execute(query)

# --- Updated checked & Updated

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

# --- Streaming quotes

def get_quote_list():
    query = "SELECT symbol FROM quote group by symbol"
    return pd.read_sql_query(query, sql_engine)    

def get_last_quote(symbol:str):
    query = "SELECT symbol, close, currency FROM quote WHERE symbol = '"+symbol+"' order by date desc limit 0,1"
    return pd.read_sql_query(query, sql_engine)

def put_quote(quote:dict, currency:str):
    quoteToInsert = {'date':datetime.fromtimestamp(quote['timestamp']).strftime("%Y-%m-%d"), \
            'symbol':quote['symbol'],
            'open':quote['open'],
            'high':quote['dayHigh'],
            'low':quote['dayLow'],
            'close':quote['price'],
            'currency':currency,
            'checked':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated':datetime.fromtimestamp(quote['timestamp']).strftime("%Y-%m-%d %H:%M:%S")}
    put_dict_to_mysql('quote', quoteToInsert)

# --- Streaming FX

def get_fx_list():
    query = "SELECT symbol FROM fx_eur group by symbol"
    return pd.read_sql_query(query, sql_engine)    

def get_last_fx(symbol:str):
    query = "SELECT symbol, close, currency FROM fx_eur WHERE symbol = '"+symbol+"' order by date desc limit 0,1"
    return pd.read_sql_query(query, sql_engine)

def put_fx(quote:dict, currency:str):
    quoteToInsert = {'date':datetime.fromtimestamp(quote['timestamp']).strftime("%Y-%m-%d"), \
            'symbol':quote['symbol'][3:],
            'open':quote['open'],
            'high':quote['dayHigh'],
            'low':quote['dayLow'],
            'close':quote['price'],
            'currency':currency,
            'checked':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated':datetime.fromtimestamp(quote['timestamp']).strftime("%Y-%m-%d %H:%M:%S")}
    put_dict_to_mysql('fx_eur', quoteToInsert)

#---- Analytics
def get_quote_eur_list():
    query = "SELECT `symbol`, max(`date`) AS max_date, min(`date`) AS min_date FROM quote_eur group by `symbol`;"
    return pd.read_sql_query(query, sql_engine)

def get_quote_eur_timeserie(symbol:str):
    query = "SELECT `date`, `close` FROM quote_eur WHERE `symbol`='"+symbol+"' ORDER BY `date` DESC;"
    return pd.read_sql_query(query, sql_engine)

def put_dataframe_to_table(dataframe:str, table:str):
    dataframe.to_sql(name=table, con=sql_engine, if_exists = 'replace', index=False)

def get_quote_eur_timeserie_all_1y():
    query = "SELECT `symbol`, `date`, `close` FROM quote_eur WHERE `date` >= (CURDATE() - INTERVAL 1 YEAR) AND DAYOFWEEK(`date`) in (2,3,4,5,6) ORDER BY `symbol`,`date` ASC;"
    return pd.read_sql_query(query, sql_engine)