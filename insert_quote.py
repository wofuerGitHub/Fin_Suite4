""" get symbolslist from fmg """

#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_quote_serie
from mylib.investment_db import get_quote_to_insert
from mylib.investment_db import put_dict_list_to_table
from mylib.investment_db import set_quote_to_stream_only

LOG_FILE = './fin_suite4.log'

writeLog(LOG_FILE, 'Start Update Quote', id = 'UPQ')

insert_quote = get_quote_to_insert()

def update_quote(symbol:str, currency:str):
    data = get_quote_serie(getApiKey(), symbol)
    for item in data:
        print(item)
        dataToInsert = {'date':item['date'], 'symbol':symbol, 'close':item['close'], 'currency':currency}
        try:
            put_dict_list_to_table(dataToInsert, 'quote')
        except: # pylint: disable=bare-except
            writeLog(LOG_FILE, 'Symbol '+dataToInsert['symbol']+' on '+dataToInsert['date']+' not stored', id = 'UPQ')

for index,row in insert_quote.iterrows():
    symbol = row['symbol']
    currency = row['currency']
    print(symbol, currency)
    update_quote(symbol, currency)
    set_quote_to_stream_only(symbol)
    
writeLog(LOG_FILE, 'End Update Quote', id = 'UPQ')
