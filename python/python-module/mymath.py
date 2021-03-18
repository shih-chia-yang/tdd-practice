"""mymath - 自訂數學模組""" #模式的說明文字
pi=3.14159
def area(r):
    """area(r) 傳回半徑r的圓形面積 test""" #模組內函式的說明文字
    global pi
    return(pi*r**2)

# print(area(10))
# intractive mode
# Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mymath
# >>> mymath.pi
# 3.14159
# >>> mymath.area(10)
# 314.159
# >>> mymath.__doc__
# 'mymath - 自訂數學模組'
# >>> mymath.area.__doc__
# 'area(r) 傳回半徑r的圓形面積'

