""" get symbolslist from fmg """

#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_fx_eur
from mylib.investment_db import get_company_key_stats_currencies
from mylib.investment_db import put_dict_list_to_table
from mylib.investment_db import put_symbol_checked
from mylib.investment_db import put_symbol_updated

LOG_FILE = './fin_suite4.log'

writeLog(LOG_FILE, 'Start Update FX EUR', id = 'FXE')

currencyToUpdateDF = get_company_key_stats_currencies()

def update_fx(currency:str):
    data = get_fx_eur(getApiKey(), currency, timeseries = 30)
    for item in data:
        # print(item)
        dataToInsert = {'symbol':currency, 'date':item['date'], 'open':item['open'], 'high':item['high'], \
            'low':item['low'], 'close':item['close'], 'currency':'EUR'}
        put_symbol_checked(symbol = dataToInsert['symbol'], table = 'fx_eur', date = dataToInsert['date'])
        try:
            put_dict_list_to_table(dataToInsert, 'fx_eur')
            put_symbol_updated(symbol = dataToInsert['symbol'], table = 'fx_eur', date = dataToInsert['date'])
        except: # pylint: disable=bare-except
            writeLog(LOG_FILE, 'Currency '+dataToInsert['symbol']+' on '+dataToInsert['symbol']+' not stored', id = 'FXE')

for index,row in currencyToUpdateDF.iterrows():
    print(row['currency'].upper())
    update_fx(row['currency'].upper())
    
writeLog(LOG_FILE, 'End Update FX EUR', id = 'FXE')
