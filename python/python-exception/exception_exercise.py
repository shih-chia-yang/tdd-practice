import sys

try:
    print(hello)
except Exception as exception:
    print("hello is not defined")
    raise IndexError("print error")

# try:
#       程式主體區塊
#
# except 例外類型1 as 變數1:
#       處理例外類型1的程式碼
#
# except 例外類型2 as 變數2:
#       處理例外類型2的程式碼
#.
#.
#.
# except:
#       預設的例外處理程式碼
#
#
#else:
#       else區塊
#
#finally:
#       finally區塊

