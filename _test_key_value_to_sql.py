#!/usr/bin/python3

import pandas as pd
import sqlalchemy as sql

USER = 'fmg'
PW = 'fmg'
HOST = '127.0.0.1'
DB = 'fmg'

CONNECTION_STRING = 'mysql://'+USER+':'+PW+'@'+HOST+'/'+DB+''
sql_engine = sql.create_engine(CONNECTION_STRING)

table = 'test'

dict = {
  "brand": "Ferrari",
  "model": "968",
  "year": 1978
}

print(input)

columns = "`%s`" % '`, `'.join(dict.keys())    # string build on column names
placeholders = ', '.join(['%s'] * len(dict))  # string build %s based on number of colums
on_duplicate = "`%s`" % '` = %s, `'.join(dict.keys())    # string build on column names
on_duplicate = on_duplicate + ' = %s'
sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON DUPLICATE KEY UPDATE %s" % (table, columns, placeholders, on_duplicate)
sql_engine.execute(sql, list(dict.values()) + list(dict.values()))