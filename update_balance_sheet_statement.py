#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.investment_db import get_company_key_stats_overview
from mylib.investment_db import put_dict_list_to_table
from mylib.investment_db import put_symbol_checked
from mylib.investment_db import put_symbol_updated
from mylib.financial_modeling_prep import get_balance_sheet_statement

LOG_FILE = 'fin_suite4.log'

writeLog(LOG_FILE, 'Start Update Balance Sheet Statement')

df = get_company_key_stats_overview()
for index, row in df.iterrows():
    symbol = row['symbol']
    print(symbol)
    data = get_balance_sheet_statement(symbol, getApiKey())
    put_symbol_checked(symbol, 'balancesheetstatement')
    try:
        for item in data:
            put_dict_list_to_table(item, 'balancesheetstatement')
        put_symbol_updated(symbol, 'balancesheetstatement')
    except:
        pass

writeLog(LOG_FILE, 'End Update Balance Sheet Statement')