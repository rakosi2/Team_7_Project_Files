import xml.etree.ElementTree as ET #importing the parsing tool ElementTree as the variable ET
from array import *
import requests, zipfile, io, os, glob
from datetime import datetime, timedelta

#####################################################################################################################################
######################################## Constucting the CAISO query URL ############################################################
#####################################################################################################################################

previous_day = datetime.now() +  timedelta(-1) #getting the date for the previous day
yesterday = previous_day.strftime('%Y%m%d') #storing the previous day in the variable 'yesterday' with the format YYYddMM (the format CAISO uses for the query)
path = "E:/As of 11.17.2020/School/2021 Spring/EE 496/Energy Management System/Project Code/" #where the file will be stored, will be different for the Raspbery Pi

start_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&" #beginning of the URL, does not change

start_date = "startdatetime=" #part of the URL that will tell CAISO what the start date is

start_time = "T00:00-0000&" #start time, does not change

end_date = "enddatetime=" #part of the URL that will tell CAISO what the end date is

end_time = "T23:00-0000&" #end time, does not change

end_url = "&version=1&market_run_id=DAM&node=STREAMVW_6_N001" #end of the URL, does not change unless you want to change the node

CAISO_query = start_url + start_date + yesterday + start_time + end_date + yesterday + end_time + end_url #constucting the whole URL

#####################################################################################################################################
######################################## Getting the .xml file from CAISO ###########################################################
#####################################################################################################################################

r = requests.get(CAISO_query) #using python requests to access the URL, content stored in the variable 'r'
z = zipfile.ZipFile(io.BytesIO(r.content)) #get the .zip file from 'r' and store it in 'z'
z.extractall() #extract the contents of that .zip file which is an .xml file, using this method doesn't save the intial .zip file, just the .xml file that was inside


list_of_files = glob.glob(path + '*xml') #from our list of files in the path, only pull the files that end with .xml

latest_file = max(list_of_files, key=os.path.getctime) #pull that latest .xml file we downloaded

#####################################################################################################################################
#####################################3##### Pulling the correct data from the .xml file #############################################
#####################################################################################################################################

tree = ET.parse(latest_file) #pulling the .xml file and storing it in 'tree'
root = tree.getroot() #need this to access everything in the XML file

temp_time = [] #temp array for the time aka the itnerval hour
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
############################################ Sorting the pulled data ################################################################
#####################################################################################################################################

time = [int(x) for x in temp_time] #casting the time into an int whilst putting it into a new list called time
cost = [float(x) for x in temp_cost] #casting the cost into a float whilst putting it into a new list called cost
sort_cost = [float(x) for x in temp_cost] #casting the cost into a float whilst putting it into a new list called sort_list

sort_cost.sort() #sort the sort_cost list

threshold = sort_cost.pop(19) #set the threshold to the the sorted cost in the 19th position

combined = list(zip(time, cost)) #combine the time and cost lists into a 2D list

sorted_list = sorted(combined) #sort the combined list

#sorted_list(time, cost) = sorted_list(t, c)
for t, c in sorted_list: #for the t, c in the sorted list

   if c >= threshold: #if c is greater than or equal to our threshold, then print out the statment
      print("Threshold of", threshold, " passed at", f'Hour {t}')