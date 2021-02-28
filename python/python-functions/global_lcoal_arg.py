x=5
def func_1():
    x=3

def func_2():
    global x 
    x=2

func_1()
print(x)
func_2()
print(x)

#修改全域變數與區域變數
g_var=0
n1_var=1
print(f'top level ->g_var:{g_var} n1_var:{n1_var}')

def test():
    n1_var =2 #test中的區堿變數
    print(f'level 1 ->g_var:{g_var} n1_var:{n1_var}')
    def inner_test():
        global g_var #指向line:13 的g_var
        nonlocal n1_var #指向上一層line:19的n1_var
        g_var=1 #line:13 g_var更改為1
        n1_var=4 #line:19 n1_var更改為4，不會影響到line:15 n1_var
        print(f'level 2  ->g_var:{g_var} n1_var:{n1_var}')
    inner_test()
    print(f'level 1 ->g_var:{g_var} n1_var:{n1_var}')

test()
print(f'top level ->g_var:{g_var} n1_var:{n1_var}')

#讀取全域變數與區域變數
#讀取函式外部的變值值，無需將變數宣告為global或nonlocal，python在函式內部找不到某變數時，會逐層往上查找

a="one"

def func():
    print(a)
    a=1 #變數a有賦值動作，視為區域變數

#將變數參照函式
#python中若只有寫函式名，代表函式本身，若寫成函式名()，則代表要執行
def f_to_num(arg):
    if int(arg):
        print(arg)

number=f_to_num
number(2)

