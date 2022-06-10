#!/usr/bin/python3

from mylib.getApiKey import getApiKey
from mylib.writeLog import writeLog
from mylib.financial_modeling_prep import get_company_key_stats
from mylib.investment_db import get_financial_statement
from mylib.investment_db import put_company_key_stats
from mylib.investment_db import put_company_key_stats_checked
from mylib.investment_db import put_company_key_stats_updated

LOG_FILE = 'fin_suite4.log'

data = get_company_key_stats('KSU^', getApiKey())
print(data)
data = get_company_key_stats('ATS.VI', getApiKey())
print(data)

