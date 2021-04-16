
import sys
sys.path.append('.././../python')
import main_module

main_module.create_divider(" print type",1,symbol='*')
print('type(value)')
print(type('hello world'))
print(type(7))

print(type(True))
print(type(False))

print(type('True'))
print(type('False'))

main_module.create_divider("# what's bool to object ",1,symbol='*')
main_module.create_divider("1. empty string :false",align="<",symbol=' ')
main_module.create_divider("2 .0;0.0;0+0j:false",align="<",symbol=' ')
main_module.create_divider("3. empty list [] :false",align="<",symbol=' ')
main_module.create_divider("4. emtpy tuple () :false",align="<",symbol=' ')
main_module.create_divider("5. emtpy {} dict :false",align="<",symbol=' ')
main_module.create_divider("6. special None :false",align="<",symbol=' ')

main_module.create_divider("# bool(str) ",1,symbol='*')
print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('hello world!'))

main_module.create_divider("# bool(int) ",1,symbol='*')
print(bool(7))
print(bool(1))
print(bool(0))
print(bool(-1))

main_module.create_divider("# equqlity ",1,symbol='*')
print(1+1==3)
print(1+1==2)

main_module.create_divider("# greater or less or equal",1,symbol='*')
print(3==4)
print(3!=4)
print(3>4)
print(3<4)
print(3>=4)
print(3<=4)

first_number=5
second_number=0
true_value=True
false_value=False

if (10>first_number>1):
    print('the value os between 1 and 10')
if(first_number>1 or second_number>1):
    print('at least one value is greater then 1')

print(not true_value)
print(not false_value)

if not first_number >1 and second_number<10:
    print('both values pass the test')
else:
    print('both values to not pass the test')
