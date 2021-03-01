"""module: test module"""
# function前加入_底線開頭命名，可避免from module import *匯入該名稱
def f(x):
    return x
def _g(x):
    return x
a=4
_b=2

#question
#假設您有一個名為new_math的模式，其中含有一個new_divide()函式，你可以用那方法匯入使用該函式
#每種方法的優缺點是什麼
#1.將此檔案與主程式放置同一個資料夾
#2.修改PYTHONPATH環境變數，使python預設搜尋資料夾增加new_math所在目錄
#3.增.pth檔設定模組路徑


#new_math模組內有一個函式叫做_helper_math()，請說明底線字元將如何影響_helper_math()的匯入方式
#A: 當使用from new_math import *時，不會匯入私有函式，若需要使用，需特別指定
