# generator functions 是一種特殊的函式，可用來自訂一個可走訪的物件
# 定義產生器函式時，必須用yield關鍵字傳回每次走訪的值，當不再有yield傳回值
# 遇到空的return敘述或遇到函式結尾，產生器就會停止。普通函式的區域變數會在
#跳出函式後消失，但是產生器函式的區域變數值會持續保存到下一次呼叫。

from itertools import count


def count_to_four():
    x=0
    while x<4:
        print("in generator,x=",x)
        yield x
        x+=1

for i in count_to_four():
    print(i)

print(2 in count_to_four())