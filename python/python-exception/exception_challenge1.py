
from ast import withitem


nums=[]
while len(nums)<2:
    num=input(f'輸入第{(len(nums)+1)}個數字 :')
    if num.isnumeric():
        nums.append(int(num))

try:
    num1,num2=tuple(nums)
    division=num1 / num2
except TypeError as error:
    print(error)
except ZeroDivisionError as zero_error:
    print(zero_error.__doc__)
else:
    print(division)
finally:
    print("division done")
