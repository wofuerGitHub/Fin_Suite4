#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_symbols_list
from mylib.investment_db import put_symbols_list
from mylib.investment_db import put_symbols_list_checked
from mylib.investment_db import put_symbols_list_updated

LOG_FILE = './fin_suite4.log'

writeLog(LOG_FILE, 'Start Update Symbols List')

data = get_symbols_list(getApiKey())
for item in data:
    print(item['symbol'])
    put_symbols_list_checked(item['symbol'])
    try:
        put_symbols_list(item)
        put_symbols_list_updated(item['symbol'])
    except:
        pass

writeLog(LOG_FILE, 'End Update Symbols List')