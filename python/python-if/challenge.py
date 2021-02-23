# print()
ans=input('Would you like to continue?')
if ans in ('no','n'):
    print('Exiting')
elif ans in ('yes','y'):
    print('Continuing...')
    print('COmplete!')
else:
    print('Please try again and respond with yes or no')