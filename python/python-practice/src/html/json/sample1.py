import json
from os import WIFCONTINUED
import requests
from pprint import pprint as pp
response=requests.get(r"https://data.cityofchicago.org/resource/6zsd-86xi.json?"
                                    r"$where=date between '2019-01-10T12:00:00'and '2019-01-10T13:00:00'")
jsondata=response.json()
# pp(jsondata)

#dump()將轉換後的json資料寫入檔案
#dumps()以字串傳回轉換後的json資料
output_path="../../sample/data_01.json"
with open(output_path,'w') as outfile:
    json.dump(jsondata,outfile,indent=2)
#使用indent 設定縮排
print(json.dumps(jsondata,indent=2))


#將list物件放入dict中，將dict轉為json物件來儲存
weather_list=[["a","b"],2,3,5,6,7,8]
outfile_path1="../../sample/data.json"
with open(outfile_path1,'w') as outfile:
    weather_obj={"reports":weather_list,"count":len(weather_list)}
    json.dump(weather_obj,outfile)

#讀取
#當資料量小時，這是簡便的方法
with open(outfile_path1,'r') as readfile:
    weather_obj=json.load(readfile)
    print(weather_obj)

#大量資料，可以對每筆資料都使用一次json.dump()，這將產生一個包含多筆json資料的檔案