import pandas as pd
import numpy as np
from sqlalchemy import false

# http://pandas.pydata.org

print(f'{"二維陣列":=^80}')
grid=[[1,2,3],[4,5,6],[7,8,9]]
print(grid)
print(f'{"使用pandas.DataFrame":=^80}')
df=pd.DataFrame(grid)
print(df)
print(f'{"pandas.DataFrame為每個欄位命名one,two,three":=^80}')
df=pd.DataFrame(grid,columns=["one","two","three"])
print(df)
#為欄位命名的好處是能夠按名稱選擇你想要的欄位，例如，只想要two這一欄的內容
print(f'{"pandas.DataFrame取得two欄資料":=^80}')
print(df["two"])
print(f'{"指定two欄資料使用comprehension產生list，不易閱讀":=^80}')
print([ x[1] for x in grid])
print(f'{"pandas.DataFrame使用迴圈巡訪 for x in df[""two""]":=^80}')
for x in df["two"]:
    print(x)
print(f'{"pandas.DataFrame取得多個欄位":=^80}')
edges=df[["one","three"]]
print(edges)
print(f'{"每個項目都加2，可以使用add()":=^80}')
print(edges.add(2))
print(f'{"pandas 載入資料,讀取json資料":=^80}')
mars=pd.read_json("./mars_data_01.json")
print(mars)
print(f'{"pandas 載入資料,讀取csv資料":=^80}')
temp=pd.read_csv("../python-practice/sample/temp_data.csv")
print(temp)
print(f'{"pandas 載入資料,將不是數值的資料替換成NaN":=^80}')
temp=pd.read_csv("../python-practice/sample/temp_data.csv",na_values=['Missing'])
print(temp)
print(f'{"pandas 儲存資料,to_csv() df.to_csv(""df_out.csv"",index=False)":=^80}')
df.to_csv("df_out.csv",index=False)
print(f'{"pandas 儲存資料,to_csv(data.json) df.to_json()":=^80}')
df.to_json("data.json")
print(f'{"使用DataFrame來整理資料":=^80}')
#header=0 : 讓pandas不要讀取csv的欄位名稱
#names=range(18) : 用range()函式產生的數字來設定欄位名稱為0~17
#usecols=range(4,18) : 用range()函式產生的數字讓read_csv()只讀取4~17欄位

temp=pd.read_csv("../python-practice/sample/202012151000.csv", header=0,names=range(9),usecols=range(2,9))
temp[5]=temp[5].div(100)
print(temp)
print(temp[5].sum())
print(temp[5].mean())
print(temp[5].median())
print(temp[5].max())
print(temp[5].min())
temp[[2,3]].groupby[[5]].sum().plot.bar()