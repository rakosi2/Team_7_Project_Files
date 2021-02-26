#!/usr/bin/python3
import requests
import time
import shutil


response = requests.get("http://oasis.caiso.com/oasisapi/SingleZip?queryname=SLD_FCST&market_run_id=DAM&startdatetime=20160415T07:00-0000&enddatetime=20160416T07:00-0000&version=1")


print('')
print('The response code is:', response.status_code)




print('\nThis is the end of the program')

