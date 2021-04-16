
import sys
sys.path.append('../../../python')
from main_module import create_divider

create_divider("return odd number between 1 and 100",1,"-")

odd_number=[odd for odd in range(100) if odd %2>0]
print(odd_number)


create_divider("use comprehension build a dict",0,"-")
create_divider("key are 11 to 15",0,"-")
create_divider("value are key number square",0,"-")

nums={num:num*num for num in [11,12,13,14,15]}
print(nums)