#using os

import os
print(os.getcwd())
print(os.curdir)
print(os.listdir(os.curdir))
print(os.path.join('bin','utils','disktools'))

#using 
#basename指路徑最後的目錄或檔案名稱
#os.path.spilt 會將basename與路徑其餘部份拆開，以tuple回傳
CRED='\033[91m'
print(CRED,os.path.split(os.path.join('some','directory','path.jpg')))
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
#os.path.basename()
print(os.path.basename(os.path.join('some','directory','path.jpg')))
#os.path.dirname()
print(os.path.dirname(os.path.join('some','directory','path.jpg')))
#os.path.spiltext()，取得副檔名
print(os.path.splitext(os.path.join('some','directory','path.jpg')))
#os.path.abspath()，取得絕對路徑
#os.path.commonprefix([path1,path2])，找出所有路徑共同的前面部份

#目前目錄
print(os.curdir)
#上一層目錄
print(os.pardir)
#作業系統名稱
print(os.name)

root_dir=""
if os.name=='posix':
    root_dir="/"
elif os.name=='nt':
    root_dir="c:\\"
else:
    print("無法識別目前作業系統")

print(root_dir)

