def calculate(x,y,z):
    return (x+y)*z

print(calculate(3,2,2))
print(calculate('foo','bar',2))
print(calculate([1,2],[3,4],2))

#函式不會檢查傳入參數的型別，只要物件可以被for迴圈走訪
#就可以用sorted排序

#只要物件可以支援+與x運算符，就可以使用calculate()函式來處理
#若自訂一個能支援+與x 的檔物物件，那calculate函式不用修改就能用來處理檔案

#如果傳入calculate()函式的物件不支援+與x
#使用EAFP搭配例外機制處理
try:
    calculate('foo','bar','fxx')
except TypeError as error:
    print(f"{calculate.__name__}發生錯誤",error)