
#define function 'def' keyword
# a pair parentheses symbols (), input parameters are defined within these parantheses
# a colon symbol : to end the function's signature

def say_hello(name='world',greeting=None):
    if greeting==None:
        print(f'hello {name}!')
    else:
        print(f'{greeting} {name}!')

def add_two_numbers(x,y):
    return x+y

def create_deck():
    suits=["hearts","spades","clubs","diamonds"]
    ranks=["2","3","4","5","6","7","8","9","10","jack","queen","kind","ace"]
    cards=[]
    for suit in suits:
        for rank in ranks:
            cards.append(f'{rank} of {suit}')
    
    return cards

value=1

def some_function():
    value=10
    return value

say_hello()
say_hello('Bob')
say_hello(greeting='howdy')
say_hello('Bob','howdy')

add_two_numbers(4,6)
result=add_two_numbers(5,7)
print(result)

# code from the previous steps and add a new function that returns a list

my_deck=create_deck()
print(my_deck)

print(value)
some_function()
print(value)


