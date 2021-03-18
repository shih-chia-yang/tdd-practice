from email import header
import json
import pandas as pd
from pprint import pprint
from pytest import param
import requests
from sqlalchemy import column

line_token = "Q6r9xXnHY7oddOrynsuwA7y0DJzdEAbqPX9VzBN3df0"

opendata_url=r"http://opendata.epa.gov.tw/api/v1/AQI?%24skip=0&%24top=1000&%24format=json"

aqi_columns=['AQI','CO','CO_8hr','County','Latitude','Longitude','NO','NO2',
'NOx','O3','O3_8hr','PM10','PM10_AVG','PM2.5','PM2.5_AVG','Pollutant',
'PublishTime','SO2','SO2_AVG','SiteId','SiteName','Status','WindDirec','WindSpeed']
last_aqi=0
last_status=""

def api_request(url):
    aqi_response=requests.get(url,verify=False)
    return aqi_response.json()

def output_to_csv(text):
    aqi=pd.DataFrame(text,columns=aqi_columns)
    aqi.to_csv("aqi.csv")

def extract(aqi):
    selected_col=aqi[['SiteName','PublishTime','Status','AQI','PM2.5']]
    filter=selected_col[(selected_col.SiteName=='古亭') &(selected_col.AQI>50)]
    site,time,status,aqi,pm = [tuple(x) for x in filter.values][0]
    message=f"時間:{time},位置:{site},空氣品質{status},目前AQI指數:{aqi},PM2.5 :{pm}"
    if aqi>=30:
        print(f"準備傳送警告到line，訊息內容：{message}")
        line_notify(message)
    print(message)

def line_notify(message):
        headers={
            "Authorization":"Bearer "+line_token,
            "content-type":"application/x-www-from-urlencoded"
        }
        payload={'message':message}
        requests.post("https://notify-api.line.me/api/notify",headers=headers,params=payload)

def read_aqi_csv():
    try:
        aqi =pd.read_csv("./aqi.csv")
        extract(aqi)
    except IOError:
        aqi_data=api_request(opendata_url)
        output_to_csv(aqi_data)
        read_aqi_csv()

def main():
     read_aqi_csv()

if __name__=="__main__":
    main()