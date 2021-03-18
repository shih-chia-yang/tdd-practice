#使用http/https下載
#python requests
#linux curl wget
import requests,sys

yearlist={}
each_year_avg_rain={}
each_year_max_tmp={}
each_year_min_tmp={}

def get_data(url):
    response=requests.get(url)
    return response.text

def clear_data(content:str):
    lines=content.split("\r\n")[7:]
    for line in lines:
        extract(line)

def calculate():
    for year in yearlist.keys():
        months=yearlist[year]
        max_temp=max([float(month[1])  for  month in months])
        min_temp=min([float(month[2])  for  month in months])
        rains=[float(month[4])  for  month in months]
        avg_rains=round(sum(rains)/len(rains),2)
        each_year_avg_rain[year]=avg_rains
        each_year_max_tmp[year]=max_temp
        each_year_min_tmp[year]=min_temp

def get_detail(line):
    fields=[x for x in line.split(" ") if x][0:7]
    year,month,max,min,af,rain,sun= tuple(fields)
    return year,month,max,min,af,rain,sun

def extract(line):
    global yearlist
    year,month,max,min,af,rain,sun= get_detail(line)
    if year not in yearlist:
        yearlist[year]=[[month,max,min,af,rain,sun]]
    else:
        yearlist[year].append([month,max,min,af,rain,sun])

def main():
    data=get_data("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")
    clear_data(data)
    calculate()
    print(each_year_avg_rain)
    print(each_year_max_tmp)
    print(each_year_min_tmp)

if __name__ == '__main__':
    main()



