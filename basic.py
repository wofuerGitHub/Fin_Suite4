#!/usr/bin/python3

import pandas as pd
import sqlalchemy as sql

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.investment_db import get_company_key_stats_overview
from mylib.financial_modeling_prep import get_income_statement
from mylib.financial_modeling_prep import get_balance_sheet_statement
from mylib.financial_modeling_prep import get_cash_flow_statement

USER = 'fmg'
PW = 'fmg'
HOST = '127.0.0.1'
DB = 'fmg'

CONNECTION_STRING = 'mysql+pymysql://'+USER+':'+PW+'@'+HOST+'/'+DB+''
sql_engine = sql.create_engine(CONNECTION_STRING)

LOG_FILE = 'fin_suite4.log'

writeLog(LOG_FILE, 'Start Basic')

income_statement = pd.DataFrame.from_dict(get_income_statement('AAPL', getApiKey()))
balance_sheet_statement = pd.DataFrame.from_dict(get_balance_sheet_statement('AAPL', getApiKey()))
cash_flow_statement = pd.DataFrame.from_dict(get_cash_flow_statement('AAPL', getApiKey()))

income_statement.to_sql('incomestatement', con=sql_engine, if_exists = 'replace', index=False)
balance_sheet_statement.to_sql('balancesheetstatement', con=sql_engine, if_exists = 'replace', index=False)
cash_flow_statement.to_sql('cashflowstatement', con=sql_engine, if_exists = 'replace', index=False)

print(income_statement)

"""
df = get_company_key_stats_overview()
for index, row in df.iterrows():
    symbol = row['symbol']
    print(symbol)
    data = get_company_key_stats(symbol, getApiKey())
    put_company_key_stats_checked(symbol)
    try:
        for item in data:
            put_company_key_stats(item)
        put_company_key_stats_updated(symbol)
    except:
        pass
"""

writeLog(LOG_FILE, 'End Basic')