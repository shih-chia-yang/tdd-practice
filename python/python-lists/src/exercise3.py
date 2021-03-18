
import sys
sys.path.append('../../../python')
from main_module import create_divider


create_divider('tuple unpacking',1,"*")

numlist=[(1,2),(3,7),(9,5)]
result=0
for num1,num2 in numlist:
    result=result+(num1*num2)

print(result)

create_divider('delete all nagative number',1,"*")

x_list=[1,3,5,0,-1,3,-2]
non_nagative_list=[x for x in x_list if x>=0]
print(non_nagative_list)


create_divider('please sum this list nagative number',1,"*")

y_list=[[1,-1,0],[2,5,-9],[-2-3,0]]
nagative_sum=sum([item for sublist in y_list for item in sublist if item <0])
print (nagative_sum)

create_divider('x<5 display "very low"',0,"*")
create_divider('-5>x>0 display "low"',0,"*")
create_divider('x=0 display "neutral"',0,"*")
create_divider('0>x>5 display high',0,"*")
create_divider('x>5 display "very high"',0,"*")




x=""
while True:
    try:
        x=int(input('input a number :'))
        break
    except ValueError:
        print("please input a number")
        continue

if x < -5:
    print("very low")
elif -5<x<0:
    print("low")
elif x == 0:
    print("neutral")
elif 0<x<5:
    print("high")
else:
    print("very high")

