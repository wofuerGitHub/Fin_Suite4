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

while True:
    print('Isin, Comany Name or Symbol:')
    search = input()

    query = "call fmg.find_dataset('"+search+"');"
    result = pd.read_sql_query(query, sql_engine)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(result)

    print('Correct Data:')
    data_line = input()
    symbol = result.iloc[[data_line]]['symbol'].values[0]
    currency = result.iloc[[data_line]]['currency'].values[0]

    print('Correct ISIN:')
    isin_line = input()
    if isin_line.isdigit():
        isin = result.iloc[[isin_line]]['isin'].values[0]
    else:
        isin = ""

    print("Symbol:  ", symbol)
    print("ISIN:    ", isin)
    print("Currency:", currency)
    print("")
    print('Update (y/n):')
    update = input()

    if update.lower() == 'y':
        query = "INSERT INTO referencedata (`symbol`, `isin`, `currency`, `updated`) values ('"+symbol+"','"+isin+"','"+currency+"',NOW()) ON DUPLICATE KEY UPDATE `isin`= '"+isin+"', `currency`='"+currency+"', `updated`=NOW();"
        sql_engine.execute(query)
        print("inserted")
    else:
        print("passed")