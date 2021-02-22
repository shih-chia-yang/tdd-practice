
# python是dynamic lan，參數不需另外宣告，但在使用時機需準確保握並且轉換為正確型別
import random

ans=random.randint(1,5)
guess=0
count=0

while guess!=ans:
    count+=1
    guess=input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess=int(guess)
else:
    print(f' you guessed it in {count} tries!')


