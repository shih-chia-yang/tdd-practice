
#將變數參照函式
#python中若只有寫函式名，代表函式本身，若寫成函式名()，則代表要執行
def f_to_num(arg):
    if int(arg):
        print(arg)

number=f_to_num
number(2)

#將函式作為引數傳遞給函式

def print_num(num):
    print(num)

def num_generator(size,func):
    for i in range(size):
        func(i)

num_generator(10,print_num)