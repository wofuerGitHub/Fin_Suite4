""" update quotes from fmg """

#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_quote
from mylib.investment_db import get_quote_list
from mylib.investment_db import put_quote
from mylib.investment_db import get_last_quote

LOG_FILE = './fin_suite4.log'

writeLog(LOG_FILE, 'Start Update Quote Stream', id = 'UQS')

while True:
    symbolsToQuery = get_quote_list()

    for index, row in symbolsToQuery.iterrows():

        symbolToQuery = get_last_quote(row['symbol'])

        print(symbolToQuery.iloc[0]['symbol'], symbolToQuery.iloc[0]['currency'])
        quote = get_quote(getApiKey(), row['symbol'])
        put_quote(quote, symbolToQuery.iloc[0]['currency'])

writeLog(LOG_FILE, 'Stop Update Quote Stream', id = 'UQS')
