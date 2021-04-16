from importlib.resources import open_binary
from pathlib import Path

#使用close()方法關閉物件
test_file_path=Path("./tests/n2w.py")
file_content=open(test_file_path)
line=file_content.readline()
#...進行動作...
file_content.close()

#opne()函式, first args is path name,second arg is operation pattern: r/w/a
#pattern 
# r:唯讀模式
# w:寫入模式
# a:以附加模式，新資料將會附加在原有資料後面

# with 使用with context manager管理open()函式開啟的檔案，
    # 管理器可用來確保檔案得到妥善處理，用完自動關閉
    # 建議使用此方式開啟檔案
with open(test_file_path,'r') as file_content:
    #readline()讀取檔案的一行字串
    one_line =file_content.readline()
    print(one_line)
    #read(n)，由目前位置讀取n個字元
    #若無指定n，則讀取全部內容
    all_content=file_content.read()
    print(all_content)

new_file_path=Path("./tests/sample.txt")

with open(new_file_path,'r') as read_new_file:
    with open(new_file_path,'w') as new_file:
         new_file.write("hello world")
    read_line=read_new_file.read()
    print(read_line)
#open()第三個參數是用來設定檔案的讀寫緩衝區
#buffering是將需要讀寫的資料暫存在記讀體中，直到達到足夠的資料量時
#再一次執行實際的I/O動作，以減少實體上磁碟機存取的次數及時間

#使用 encodeing 指定檔案的編碼方式
#open('myfile',encoding='utf-8')

#計算檔案行數
count=0
with open(test_file_path,'r') as py_read:
    while py_read.readline() is not "":
        count+=1
print(count)

# refactor
with open(test_file_path,'r') as py_read:
    count=len(py_read.readlines())
print(count)


#for 迴圈逐行讀取檔案
count=0
with open(test_file_path) as py_read:
    for line in py_read:
        count+=1
print(count)

#處理換行符號
#windows '\r\n'
#macintosh '\r'
#linux/unix '\n'

#python讀取檔案時會自動將不同系統的換行符號統一轉換為'\n'
#若有需要，可以在開啟檔案時，用newline參數強制設定要作為換行符號的字串

with open(test_file_path,newline="\n") as py_read:
    pass


with open(test_file_path,'r') as py_read:
    lines = py_read.readlines()
    with open(new_file_path,'w') as txt_write:
        txt_write.writelines(lines)

#使用二進制模式
#將檔案中所有資料讀到一個bytes物件中，特別是資料不是字串
#希望將全部資料存到記憶體中，視為一連串位元組byte所成的資料序列
#open()的模式參數加b

with open(test_file_path,'rb') as py_read_byte:
    header=py_read_byte.read(4)
    data=py_read_byte.read()
print(header)
print(data)
