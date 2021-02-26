#!/usr/bin/python3
import requests
import time
import shutil
import json
import datetime

todays_date = datetime.datetime.now()
yesterdays_date = todays_date - datetime.timedelta(days = 1)
tomorrows_date = todays_date + datetime.timedelta(days = 1)
string_tail = 'T07:00-0000'

first_url_string = todays_date.strftime("%Y") + todays_date.strftime("%m") + todays_date.strftime("%d") + string_tail
second_url_string = tomorrows_date.strftime("%Y") + tomorrows_date.strftime("%m") + tomorrows_date.strftime("%d") + string_tail

print("1st url string: ", first_url_string)
print("2nd url string: ", second_url_string)


response = requests.get("http://oasis.caiso.com/oasisapi/SingleZip?queryname=SLD_FCST&market_run_id=DAM&startdatetime=20160415T07:00-0000&enddatetime=20160416T07:00-0000&version=1")


print('The response code is:', response.status_code)



