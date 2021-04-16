import random
min=0
max=10
ans=random.randint(min,max)
guess=0
count=0
print(f'Guess a number between {min} and {max}')

while guess!=ans:
    count+=1
    guess=input(f'Enter guess #{count}: ')
    if guess.isnumeric():
        guess=int(guess)
        if(guess < ans):
            print('Your guess is too low, try again!')
        elif guess> ans:
            print('Your guess is too high, try again!')
    else:
        print('Numbers only, please!')
else:
    print(f'you guessed it in {count} tries!')