#LBYL 事先檢查避免出錯
# Look Before You Leap
#assert 運算式,參數
#等價
# if __debug__:
#   if not 運算式:
#       raise AssertionError(參數)

# x=(1,2,3)
# assert len(x)>5 ,"發生錯誤,len(x) 小於等於 5"

num=""
while isinstance(num,str):
    num=input("請輸一個數字: ")
    if num.isnumeric():
        num=int(num)
    assert num !=0 ,"數字不可輸入0"

