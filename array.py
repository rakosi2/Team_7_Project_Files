from array import *
import xml.etree.ElementTree as ET #importing the parsing tool ElementTree as the variable ET

tree = ET.parse('tester.xml') #pulling the XML file and storing it in 'tree'
root = tree.getroot() #need this to access everything in the XML file

i = 1
temp = []
hour = []

# for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}REPORT_DATA"): #go into the REPORT_DATA
   
#    hour = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM").text #go into the INTERVAL_NUM to get the hour of the day
#    price = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE").text #find the price of energy
#    #temp.insert(int(hour), price)
#    print(hour, price) #print the corresponding hour and its energy price



# while i <= 24:
#    print(i)
#    i+=1

# while i <= 24:
#    for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}REPORT_DATA"): #go into the REPORT_DATA
   
#       hour = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM").text #go into the INTERVAL_NUM to get the hour of the day
#       price = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE").text #find the price of energy
#       #temp.insert(int(hour), price)
#       print(hour, price) #print the corresponding hour and its energy price
#    i+=1

# for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}REPORT_DATA"): #go into the REPORT_DATA
#    while i <= 24:
#       hour = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM").text #go into the INTERVAL_NUM to get the hour of the day
#       price = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE").text #find the price of energy
#       #temp.insert(int(hour), price)
#       print(hour, price) #print the corresponding hour and its energy price
#       i+=1

for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}REPORT_DATA"): #go into the REPORT_DATA
   
   hour = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM").text #go into the INTERVAL_NUM to get the hour of the day
   price = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE").text #find the price of energy

   temp.append(hour)

   #print(hour, price) #print the corresponding hour and its energy price

# for x in temp:
#     for y in x:
#         print(y,end = " ")
#     print()

#print(temp[5])

#print(temp + "\n")

print(*temp, sep = "\n") #prints the array 'temp', each item is on its own line
