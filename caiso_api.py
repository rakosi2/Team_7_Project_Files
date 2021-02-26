#!/usr/bin/python3
import requests
import time
import shutil
import json
import datetime

todays_date = datetime.datetime.now()
string_tail = 'T07:00-0000'

print("1st url string: ", todays_date.strftime("%Y") + todays_date.strftime("%m") + todays_date.strftime("%d") + string_tail)
print("2nd url string: ", todays_date.strftime("%Y") + todays_date.strftime("%m") + todays_date.strftime("%d") + string_tail)


response = requests.get("http://oasis.caiso.com/oasisapi/SingleZip?queryname=SLD_FCST&market_run_id=DAM&startdatetime=20160415T07:00-0000&enddatetime=20160416T07:00-0000&version=1")


print('\nThe response code is:', response.status_code)



