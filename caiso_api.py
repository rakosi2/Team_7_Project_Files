#!/usr/bin/python3
import requests
import time
import shutil
import json
import datetime
import io
import zipfile
import os
from xml.etree import ElementTree

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
    dom = ElementTree.parse(filename)
    root = dom.getroot()
    root = root[1][0][1]
    values = [[]]
    for child in root:
        sub_string = []
        string = child.tag
        for child2 in child:
            string = child2.tag
            if(string[45:] == "INTERVAL_NUM"):
                sub_string.append(int(child2.text) - 1)
            elif(string[45:] == "INTERVAL_START_GMT"):
                sub_string.append(child2.text)
            elif(string[45:] == "INTERVAL_END_GMT"):
                sub_string.append(child2.text)
            elif(string[45:] == "VALUE"):
                sub_string.append(float(child2.text))
        values.append(sub_string)

    values = sorted(values)
    values.pop(0)
    values.pop(0)

    #####################################################################################################################################
    ############################## This portion is to get weather data ##################################################################
    #####################################################################################################################################
    file = open('weather_Api_Key.txt', 'r')
    api_key = file.read()
    file.close

    # base_url variable to store url
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat=32.7157&lon=-117.1611&exclude=current,minutely,alerts,daily&appid="

    # complete_url variable to store
    # complete url address
    complete_url = base_url + api_key


    # get method of requests module
    # return response object
    response = requests.get(complete_url)


    # json method of response object
    # convert json format data into
    # python format data
    if response.status_code == 200:
        x = response.json()     # This is a dictionary
        x = x['hourly']

    for each in range(0, 48):
        if(todays_date.day == datetime.datetime.fromtimestamp(x[each]['dt']).day and todays_date.hour == datetime.datetime.fromtimestamp(x[each]['dt']).hour):
            values[todays_date.hour].append(x[each]['clouds'])
    #####################################################################################################################################
    ############################### End of getting weather data #########################################################################
    #####################################################################################################################################
    with open('data.json', 'w') as outfile:
        json.dump(values, outfile)


if os.path.exists(filename):        # Delete the file just downloaded
    os.remove(filename)             # Delete the file just downloaded

