#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_company_key_stats
from mylib.investment_db import get_company_key_stats_overview
from mylib.investment_db import put_company_key_stats
from mylib.investment_db import put_company_key_stats_checked
from mylib.investment_db import put_company_key_stats_updated

LOG_FILE = './fin_suite4.log'

writeLog(LOG_FILE, 'Start Update Company Key Stats')

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
    
writeLog(LOG_FILE, 'End Update Company Key Stats')