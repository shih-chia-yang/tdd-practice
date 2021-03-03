import glob,os
from ntpath import join
from importlib.resources import path
# 抓出所有目錄或檔案
print(glob.glob("*"))
#抓出字尾為bkp的所有目錄或檔案
print(glob.glob("*bkp"))
#抓出主檔名只有一個字元、副檔名為tmp的所有檔案
print(glob.glob("?.tmp"))
#抓出主檔名只有一個字元0-9、副檔名為tmp的所有檔案
print(glob.glob("[0-9].tmp"))

#更名
os.rename('1.tmp','1.tmp.old')
print(os.listdir(os.curdir))
os.rename('1.tmp.old','1.tmp')

#移動
os.rename('7.tmp',os.path.join(os.pardir,'7.tmp'))
print(os.listdir(os.pardir))
os.rename(os.path.join(os.pardir,'7.tmp'),os.path.join(os.getcwd(),'7.tmp'))

dir_path=os.path.join(os.getcwd(),"testPath")
file_path=os.path.join(dir_path,"testfile.tst")
#建立新資料夾
if os.path.exists(dir_path) ==False:
    os.mkdir(dir_path)

with open(file_path,'w') as new_file:
    new_file.write("test")
os.scandir(".")

remove_paths=[file_path,dir_path]
for path in remove_paths:
    if os.path.isdir(path):
        #無法刪除資料夾, 此限制是為了安全性設計
        print(f'{path} is a directory , it can not remove by os.remove')
    else:
        os.remove(path)

#刪除資料夾 ,僅能刪除空目錄
#shutil.rmtree()函式，以遞迴方式刪除目錄中的所有子目錄與檔案
os.rmdir(dir_path)
print(f'{dir_path} removed by os.rmdir')
os.listdir(".")