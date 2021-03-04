import os

# topdown預設True，每個目錄優先處理檔案，再處理目錄，由最上層目錄開始到下層子目錄的清單
#topdown=False，優先處理每個目錄的子目錄，產生最下層子目錄開始到最上層目錄的清單
#指定followlinks=True，os.walk()才會進入 symbol link directroy
#預設忽略錯誤，如要處理錯誤，可以用onerroe=function來指定處理的函式
for entry in os.walk("../",topdown=False):
    print(entry)

#計算資料夾下的檔案數

for root,dirs,files in os.walk(os.pardir):
    print(f'{root} has {len(files)}.')

    #module suutil 
    #copytree()函式可以遞迴複製目錄中所有檔案及其所有子目錄，並保留原有存取權和最後存取/修改時間的資訊
    #rmtree() 刪除目錄及其所有子目錄
    #詳細資訊 https://docs.python.org/3/library/shutil.html
