import sys
sys.path.append('../../python')
from main_module import create_divider


create_divider('test a value for inclusion in a list',1,"*")
numbers=[1,3,5]
print(5 in numbers)
print(8 in numbers)

print(5 not in numbers)
print(8 not in numbers)

create_divider('loop through a list',1,"*")

cities=['chicage','london','tokyo']

for city in cities:
    print(city)

create_divider('break out of a for loop',1,"*")

numbers=[42,77,16,101,23,8,4,15,55]
numbers.sort()

for number in numbers:
    if number>42:break;
    print(number)

create_divider('use an else statement',1,"*")

import random
numbers=[]

while len(numbers)<5:
    numbers.append(random.randint(1,100))

for number in numbers:
    print(number)
    if(number>=90):
        print('found at one number greater than 90')
        break
else:
    print('no numbers greater than 90')

print('complete')

create_divider('use a contunue statement',1,"*")

values=["laptop",7,"phone",3,"dslr",5]
equipment=[]

for value in values:
    if isinstance(value,str)==False:
        continue
    equipment.append(value)
print(equipment)

create_divider('create nested for loops',1,"*")

suits=["hearts","spades","clubs","diamonds"]
ranks=["2","3","4","5","6","7","8","9","10","jack","queen","kind","ace"]

for suit in suits:
    for rank in ranks:
        print(f'{rank} or {suit}')

create_divider('choose randomly from a list',1,"*")

numbers=[42,77,16,101,23,8,4,15,55]
selected_number=random.choice(numbers)
print(selected_number)

selected_numbers=random.choices(numbers,k=3)
print(selected_numbers)