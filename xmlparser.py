import xml.etree.ElementTree as ET #importing the parsing tool ElementTree as the variable ET

tree = ET.parse('tester.xml') #pulling the XML file and storing it in 'tree'
root = tree.getroot() #need this to access everything in the XML file

#ET.dump(tree) #pulls the whole XML file to see if it is being stored

#pulling the text from the XML file
#for elm in root.findall(".//"):
   #print(elm.text)

# for elm in root.findall(".//"): #figuring out what the tags are
#    print(elm.tag)


#using the {http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE tag and pulling the text inside that tag
# for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE"):
#    print(elm.text)

# for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}OPR_DATE"):
#    print(elm.text)
   # for elm in root.findall("./{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM"):
   #    print(elm.text)
   #    for elm in root.findall("./{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE"):
   #       print(elm.text)

# for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM"):
#    print(elm.text)
   
# for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE"):
#    print(elm.text)

for elm in root.findall(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}REPORT_DATA"): #go into the REPORT_DATA
   
   hour = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}INTERVAL_NUM").text #go into the INTERVAL_NUM to get the hour of the day
   price = elm.find(".//{http://www.caiso.com/soa/OASISReport_v1.xsd}VALUE").text #find the price of energy

   print(hour, price) #print the corresponding hour and its energy price
