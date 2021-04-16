from pathlib import Path
import sys
#標準輸入/輸出與重新導向
# sys.stdin 標準輸入 
# sys.stdout 標準輸出
# sys.stderr 標準錯誤輸出
# 可以將這些屬性視為特別的file物件
# read() readline() readlines() 讀取
# print() wirte() writelines() 寫入
filepath=input("請輸入檔案名稱 :")
print(filepath)

print("write to the standard output .")
sys.stdout.write("write to the standard output .\n")

#將標準輸入重新導向到檔案，這樣便可以從檔案中讀取資料
#標準輸出或標準錯誤也可以重新導向，設定寫到檔案
#重新導向後，回復原始值 sys.__stdin__ ,sys.__stdout__,sys.__stderr__
test_std_file=Path("./tests/outfile.txt")
with open(test_std_file,'w') as write_file:
    sys.stdout=write_file
    sys.stdout.writelines(["a first line . \n","a second line . \n"])
    print("a line from the print function")
    sys.stdout=sys.__stdout__

#不改變標準輸出的情況下，print()函式也可以重新導向到任何檔案
with open(test_std_file,'w') as print_to_write:
    print("print first line write to file","print second line wrtite to file",file=print_to_write)

