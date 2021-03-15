#!/usr/bin/python3
import requests
import time
import shutil
import json
import datetime
import io
import zipfile
import os
import xml.etree.ElementTree as ET

todays_date = datetime.datetime.now()
yesterdays_date = todays_date - datetime.timedelta(days = 1)
tomorrows_date = todays_date + datetime.timedelta(days = 1)

string_tail = 'T07:00-0000'
first_url_string = todays_date.strftime("%Y") + todays_date.strftime("%m") + todays_date.strftime("%d") + string_tail
second_url_string = tomorrows_date.strftime("%Y") + tomorrows_date.strftime("%m") + tomorrows_date.strftime("%d") + string_tail

# base_url variable to store url
base_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP"

# first url argument
first_url_arg = "&startdatetime=" + first_url_string

# Second url argument
second_url_arg = "&enddatetime=" + second_url_string

# url_tail variable to store the tail of the url
url_tail = "&market_run_id=DAM&version=1&node=STREAMVW_6_N001"

# complete_url variable to store
# complete url address
complete_url = base_url + first_url_arg + second_url_arg + url_tail

response = requests.get(complete_url)

if response.status_code == 200:
    z = zipfile.ZipFile( io.BytesIO(response.content) )
    filename = z.namelist()[0]
    z.extractall("./")
    tree = ET.parse(filename)
    root = tree.getroot()
    
    
if os.path.exists(filename):
    os.remove(filename)

