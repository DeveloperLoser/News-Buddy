import requests
from datetime import datetime
import xml.etree.ElementTree as ET 

def updateData():
    weatherdata = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.2109&lon=-75.3674&FcstType=digitalDWML")
    newdata = open("newdata.xml", 'wb')
    newdata.write(weatherdata.content)
    newdata.close

def parseData(data): # Get the root
    tree = ET.parse(data)
    root = tree.getroot()
    return root

def calcTime(): # Get the # of hours between now and tomorrow
    now = datetime.now()
    now = now.strftime('%H')
    now = int(now)
    return(23 - now)

def gethHourlyTemp(root):
    hourlyTemperature = []
    for child in root.iter('temperature'):
        if (child.attrib).get("type") == "hourly":
            for val in child.findall("value"):
                hourlyTemperature.append(val.text)
    return hourlyTemperature

def getRain(root):
    rainchance = []
    for child in root.iter('probability-of-precipitation'):
        if (child.attrib).get("type") == "floating":
            for val in child.findall("value"):
                rainchance.append(val.text)
    return rainchance

def getWeather():
    updateData()
    root = parseData('newdata.xml')
    templist = (gethHourlyTemp(root)[0:calcTime()])
    rainlist = (getRain(root)[0:calcTime()])
    return templist, rainlist

if __name__ == "__main__":
    updateData()
    root = parseData('newdata.xml')
    print(gethHourlyTemp(root)[0:calcTime()])
    print(getRain(root)[0:calcTime()])
        