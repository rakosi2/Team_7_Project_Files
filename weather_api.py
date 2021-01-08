import requests
import json
import datetime

file = open('weather_Api_Key.txt', 'r')
api_key = file.read()
file.close

# base_url variable to store url
base_url = "https://api.openweathermap.org/data/2.5/onecall?lat=32.7760&lon=-177.0713&exclude=current,minutely,alerts,daily"

# complete_url variable to store
# complete url address
complete_url = base_url + "&appid=" + api_key

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()     # This is a dictionary
x = x['hourly']


for each in range(len(x)):
    print(  datetime.datetime.fromtimestamp(x[each]['dt']) , "  ", x[each]['clouds'], "%", sep = '' )



