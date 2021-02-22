# 1.using while statement
# 2.use the optional statements break and else 
# 3.handle case when the user enters nothing by using the continue statement
import random

roll=0
count=0

print('First person to roll a 5 wins !')
while roll!=5:

    name=input('enter a name, or \'q\' to quit:')
    if name.strip()=='':
        continue
    if name.strip()=='q':
        break

    count+=1
    roll=random.randint(1,5)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} wins !')


print(f'it took {count} rolls ro roll a 5!')


#recap 
#The while statement allows you to create a looping structure that continues to loop through a code block until a Boolean expression evaluates to False.
#Add the break statement to exit out of a code block prematurely before the Boolean expression evaluates to False.
#Add the else statement to provide a second code block that runs after the while statement's Boolean expression evaluates to False.
#Add the continue statement to skip over the remainder of the code block and set the execution path back to the Boolean expression.
