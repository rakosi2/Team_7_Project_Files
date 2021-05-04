import xml.etree.ElementTree as ET #importing the parsing tool ElementTree as the variable ET
from array import *
import requests, zipfile, io, os, glob, pprint
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
from time import sleep


#####################################################################################################################################
######################################## Setting up Raspberry Pi GPiOS ##############################################################
#####################################################################################################################################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)



#####################################################################################################################################
######################################## Constucting the CAISO query URL ############################################################
#####################################################################################################################################

next_day = datetime.now() +  timedelta(+1) #getting the date for the previous day
tomorrow = next_day.strftime('%Y%m%d') #storing the previous day in the variable 'yesterday' with the format YYYddMM (the format CAISO uses for the query)
path = "/home/pi/Code/" #where the file will be stored, will be different for the Raspbery Pi

start_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&" #beginning of the URL, does not change

start_date = "startdatetime=" #part of the URL that will tell CAISO what the start date is

start_time = "T00:00-0000&" #start time, does not change

end_date = "enddatetime=" #part of the URL that will tell CAISO what the end date is

end_time = "T23:00-0000&" #end time, does not change

end_url = "&version=1&market_run_id=DAM&node=STREAMVW_6_N001" #end of the URL, does not change unless you want to change the node

CAISO_query = start_url + start_date + tomorrow + start_time + end_date + tomorrow + end_time + end_url #constucting the whole URL

#####################################################################################################################################
######################################## Getting the .xml file from CAISO ###########################################################
#####################################################################################################################################

r = requests.get(CAISO_query) #using python requests to access the URL, content stored in the variable 'r'
z = zipfile.ZipFile(io.BytesIO(r.content)) #get the .zip file from 'r' and store it in 'z'
z.extractall() #extract the contents of that .zip file which is an .xml file, using this method doesn't save the intial .zip file, just the .xml file that was inside


list_of_files = glob.glob(path + '*xml') #from our list of files in the path, only pull the files that end with .xml

latest_file = max(list_of_files, key=os.path.getctime) #pull that latest .xml file we downloaded

#####################################################################################################################################
######################################## Pulling data from the weather API ##########################################################
#####################################################################################################################################

s = requests.get('https://api.weather.gov/gridpoints/SGX/59,15/forecast')

clouds = "Mostly Cloudy"
rain = "Chance Rain Showers"

weather_day = []
weather_type = []

x = 0

while x < 14:

    day = s.json()['properties']['periods'][x]['name']
    expected = s.json()['properties']['periods'][x]['shortForecast']
    weather_day.append(day)
    weather_type.append(expected)
    #print()
    x += 1

zipped = list(zip(weather_day, weather_type))

#####################################################################################################################################
########################################### Pulling the correct data from the CAISO .xml file #######################################
#####################################################################################################################################

tree = ET.parse(latest_file) #pulling the .xml file and storing it in 'tree'
root = tree.getroot() #need this to access everything in the XML file

temp_time = [] #temp array for the time aka the interval hour
time = [] #new arary for the time with only the time of the LMP

temp_cost = [] #temp array for the cost aka the value
cost = [] #new array for the cost with only the cost of the LMP
sort_cost = [] #array for the sorted LMP price

for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}REPORT_DATA"): #go into the REPORT_DATA

   if elm.find("{http://www.caiso.com/soa/OASISReport_v1.xsd}DATA_ITEM").text == "LMP_PRC": #find the tag called DATA_ITEM and if the text inside is LMP_PRC continue
      
      hour = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM").text #go into the INTERVAL_NUM to get the hour of the day
      price = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE").text #find the price of energy

      temp_time.append(hour) #put hour into list
      temp_cost.append(price) #put price into list


os.remove(latest_file) #delete the .xml file because we got the data from it already

#####################################################################################################################################
############################################ Sorting the pulled data from CAISO #####################################################
#####################################################################################################################################

time = [int(x) for x in temp_time] #casting the time into an int whilst putting it into a new list called time
cost = [float(x) for x in temp_cost] #casting the cost into a float whilst putting it into a new list called cost
sort_cost = [float(x) for x in temp_cost] #casting the cost into a float whilst putting it into a new list called sort_list

sort_cost.sort() #sort the sort_cost list

high_threshold = sort_cost.pop(19) #set the high threshold to the sorted cost in the 19th position

low_threshold = sort_cost.pop(4) #set the low threshold to the sorted cost in the 4th position

combined = list(zip(time, cost)) #combine the time and cost lists into a 2D list

sorted_list = sorted(combined) #sort the combined list

#####################################################################################################################################
############################################ Using all the data for the EMS algorithm ###############################################
#####################################################################################################################################

if clouds or rain in zipped.pop(1): # if there are clouds or rain in the forecast
   print("Today is " + next_day.strftime('%m/%d/%Y'))
   print("There will not be a lot of solar production today.\n") #wont be a lot of solar production
   print("Hour by hour breakdown: ")


   for t, c in sorted_list: #for the t, c in the sorted list
       
        
      if c >= high_threshold: #if c is greater than or equal to our threshold, then print out the statment
         print("- High threshold of", high_threshold, "passed at", f'Hour {t}', "use batteries to power load")
         print("- Contacts 1, 3, 4 open and Contact 2 shut\n")
         sleep(2)

      elif c <= low_threshold:
         print("- Low threshold of", low_threshold, "not passed at", f'Hour {t}', "charge the batteries")
         print("- Contacts 2, 3 open and Contacts 1, 4 shut\n")
         sleep(2)

      else:
         print("- Solar panels generating energy if sun is available and grid is powering house at", f'Hour {t}')
         print("- Contacts 1, 2, 4 open and Contact 3 shut\n")
         sleep(2)
   

else:
   print("Today is " + next_day.strftime('%m/%d/%Y'))
   print("There will be a lot of solar production today") #wont be a lot of solar production
   print()
   print("Hour by hour breakdown: ")
   
   for t, c in sorted_list: #for the t, c in the sorted list

      if c >= high_threshold: #if c is greater than or equal to our threshold, then print out the statment
         print("High threshold of", high_threshold, "passed at", f'Hour {t}', "use batteries to power load")
         print("- Contacts 1, 3, 4 open and Contact 2 shut\n")
         sleep(2)

      elif c <= low_threshold:
         print("Low threshold of", low_threshold, "not passed at", f'Hour {t}', "charge the batteries")
         print("- Contacts 2, 3 open and Contacts 1, 4 shut\n")
         sleep(2)

      else:
         print("Solar panels generating energy if sun is available and grid is powering house at", f'Hour {t}')
         print("- Contacts 1, 2, 4 open and Contact 3 shut\n")
         sleep(2)