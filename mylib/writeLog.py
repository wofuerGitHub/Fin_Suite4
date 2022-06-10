#!/usr/bin/python3

# writeLog.py
# functions for different sources to get the time series
# 16.03.2021

from datetime import datetime

def writeLog(file, message, **kwargs):
    id = kwargs.get('id', None)
    f = open(file, "a+")
    if id:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' : '+id+' : '+message+'\n')
    else:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' : '+message+'\n')
    f.close()
