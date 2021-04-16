dash_len=80
learning_obj="performs various mathematical operations"
print(f'{learning_obj:-^{dash_len}}')
first_value=5
second_value=4

sum=first_value+second_value
difference=first_value-second_value
product=first_value*second_value
quotient=first_value/second_value
modulus=first_value%second_value
exponent=first_value**second_value

print('sum: '+str(sum))
print('difference: '+str(difference))
print('product: '+str(product))
print('quotient: '+str(quotient))
print('modulus: '+str(modulus))
print('exponent: '+str(exponent))

# + addition operator
# - sumtraction operator
# * multiplication operator
# / division operator
# % modulus operator 
# ** exponent operator. for example 5 to the fourth power 5*5*5*5
learning_obj="control the default order of operations"
print(f'{learning_obj:-^{dash_len}}')
print(3+4*5)
print((3+4)*5)

learning_obj="invesitigate division more closely"
print(f'{learning_obj:-^{dash_len}}')
first_value=5
second_value=4

quotient =first_value/second_value

print(type(quotient))
print(quotient)

learning_obj="convert a float into an int"
print(f'{learning_obj:-^{dash_len}}')

pi=3.14
print(type(pi))
print(int(pi))
print(round(pi))

uptime=99.99
print(type(uptime))
print(int(uptime))
print(round(uptime))

learning_obj="rounds to a specific decimal place"
print(f'{learning_obj:-^{dash_len}}')

first_value=round(7.654321,2)
print(first_value)

second_value=round(9.87654,3)
print(second_value)