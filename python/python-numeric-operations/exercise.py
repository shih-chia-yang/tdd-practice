print(type('7'))
print(type(7))
print(type(7.1))

#<class 'str'>
#<class 'int'>
#<class 'float'>

print(isinstance('7',str))
print(isinstance(7,int))
print(isinstance(7.1,float))

print(isinstance(7,str))
print(isinstance('7',int))
print(isinstance('7.1',float))

#True
#True 
#True 
#False
#False
#False
#boolean expression same with isinstance
print(type('7')==str)

x='a string'
print(type(x))
x=7
print(type(x))
x=False
print(type(x))

first_value =int(input('First Number: '))
second_value=int(input('Second numebr: '))
sum=first_value+second_value
print("sum: "+str(sum))