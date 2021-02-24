print('type(value)')
print(type('hello world'))
print(type(7))

print(type(True))
print(type(False))

print(type('True'))
print(type('False'))

print('bool(str)')
print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('hello world!'))

print('bool(int)')
print(bool(7))
print(bool(1))
print(bool(0))
print(bool(-1))

print('equqlity')
print(1+1==3)
print(1+1==2)

print('step 6')
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