# assignment opertators
len=80;
def create_divider(title):
    length=80
    print(f'{title:-^{length}}')

create_divider('increment and assign operator')
count = 0
while count != 5:
    count += 1
    print(count)

create_divider('increment count by 3')
count = 0
while count <= 20:
    count += 3
    print(count)

create_divider('decrements count by 3')
count = 20
while count >= 0:
    count -= 3
    print(count)

#= 	Assign
#+= 	Add then assign
#-= 	Subtract then assign
#*= 	Multiply then assign
#/= 	Divide then assign
#%= 	Get the modulus then assign
#**= 	Perform exponent then assign
#//= 	Perform floor division then assign 