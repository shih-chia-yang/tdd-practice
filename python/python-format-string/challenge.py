first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
# ans is strip().lower().title()
first_value=first_value.strip().lower().capitalize()
first_value=f'{first_value:-^{len(first_value)*2}}'.replace('-',' ')


# Second challenge
second_value=second_value.replace('-','').strip().capitalize()
second_value=second_value.ljust(len(second_value))
# Third challenge
#ans is replace().replace().swapcase()
third_value=third_value.replace(' ','').replace('-',' ').lower().capitalize()
third_value=f'{third_value:>{len(third_value)*2}}'.replace('-',' ')

print(first_value)
print(second_value)
print(third_value)
# Fourth challenge - use only the print() function (no f-strings)
#ans is print() using sep='#; end='!'
print(fourth_value+'#'+fifth_value+'#'+sixth_value+'!')

# Fifth challenge - use only a single print() function.  
# Create tabs and new lines using f-strings.
#ans is print(f'\n\t{}\n\t{}\n\t{}')
print(f'{fourth_value:>{8+len(fourth_value)}}' +'\n' f'{fifth_value:>{8+len(fifth_value)}}' +'\n' f'{sixth_value:>{8+len(sixth_value)}}')