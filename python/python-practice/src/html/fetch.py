import json
from json.tool import main
import csv
import requests
import weather_context
import dto_weather

def export(headers,contents,filename):
    with open(f'./export/{filename}.csv','w') as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(contents)

def fetch(url):
    response=requests.get(url)
    jsondata=response.json()
    return jsondata['records']['locations'][0]['location']

def extract(json_data):
    city_avg={}
    for location in json_data:
        city=location['locationName']
        for element in location['weatherElement']:
            if element['elementName']=='T':
                every_city_ervery_day_avg=[]
                for every_day in element['time']:
                    starttime=every_day['startTime']
                    endtime=every_day['endTime']
                    avg=every_day['elementValue'][0]['value']
                    every_city_ervery_day_avg.append([city,starttime,endtime,avg])
                city_avg[city]=every_city_ervery_day_avg
    return city_avg

def main():
    source=fetch(r"https://opendata.cwb.gov.tw/api/v1/rest/"
                r"datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314")
    datas=extract(source)
    session=weather_context.db_init()
    for data in datas:
        headers=['縣市別','開始時間','結束時間','平均溫度']
        export(headers,datas[data],data)
        weather_context.insert(session,dto_weather.Weather,datas[data])
    session.commit()
    weathers = weather_context.select(session,dto_weather.Weather)
    for weather in weathers:
        print(weather.city,weather.start_time,weather.end_time,weather.avg_temp)
    session.close()
    
if __name__ == '__main__':
    main()