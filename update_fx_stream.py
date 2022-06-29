""" update quotes from fmg """

#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_quote
from mylib.investment_db import get_fx_list
from mylib.investment_db import put_fx
from mylib.investment_db import get_last_fx

LOG_FILE = './fin_suite4.log'

writeLog(LOG_FILE, 'Start Update FX Stream', id = 'UFS')

while True:
    symbolsToQuery = get_fx_list()

    for index, row in symbolsToQuery.iterrows():

        symbolToQuery = get_last_fx(row['symbol'])

        print(symbolToQuery.iloc[0]['symbol'], symbolToQuery.iloc[0]['currency'])
        quote = get_quote(getApiKey(), "EUR"+row['symbol'])
        put_fx(quote, symbolToQuery.iloc[0]['currency'])

writeLog(LOG_FILE, 'Stop Update FX Stream', id = 'UFS')
