#使用http/https下載
#python requests
#linux curl wget
import requests

data_row=[]
yearlist={}
every_max_tempure={}

def get_data(url):
    response=requests.get(url)
    return response.text

def clear_data(content:str):
    global yearlist
    lines=content.split("\r\n")[7:]
    for line in lines:
        fields= [x for x in line.split(" ") if x][0:7]
        year,month,max,min,af,rain,sun=tuple(fields)
        if year not in yearlist:
            data_row.append(fields)
            # yearlist.setdefault(year,data_row)
            yearlist[year]=data_row
            # yearlist[year]=data_row
            every_max_tempure.setdefault(year)
            every_max_tempure[year]=max
        else:
            yearlist[year].append(fields)
            if float(max) > float(every_max_tempure[year]):
                every_max_tempure[year]=max

data=get_data("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")
clear_data(data)
# print(every_max_tempure['2002'])
    