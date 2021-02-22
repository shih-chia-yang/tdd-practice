
#define function 'def' keyword
# a pair parentheses symbols (), input parameters are defined within these parantheses
# a colon symbol : to end the function's signature

def say_hello(name='world',greeting=None):
    if greeting==None:
        print(f'hello {name}!')
    else:
        print(f'{greeting} {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='howdy')
say_hello('Bob','howdy')


