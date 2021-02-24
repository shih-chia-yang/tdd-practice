# create a list of values
import sys
sys.path.append('../../python')
from main_module import create_divider

create_divider('create a list of values',1,"*")

colors=['red','green','bule','yellow','orange','purple','brown']
print(colors)
print(type(colors))

create_divider('it\'s\' important to understand that you can add values of any data type to a list',1,"*")

mixed_list=['jhon',3.14,7,False]
print(mixed_list)
print(type(mixed_list))

create_divider('use an index to access individual elements',1,"*")

print(colors)
#從左邊0～n，-1開始為倒數第1個
print(f'0-based indexing into the list ...second item: {colors[1]}')
print(f'last item of the list: {colors[-1]}')
print(f'next to last item in the list: {colors[-2]}')

create_divider('create a slice',1,"*")

print('\nPrint a slice,starting at index 2 and excluding index5:')
print(colors[2:5])
print(type(colors[2:5]))

print('\nprinst a slice ,starting at index 0 to 3:')
print(colors[0:3])
print(type(colors[0:3]))

print('\nprint a slice,starting at index 4 to the end of the last:')
print(colors[4:])
print(type(colors[4:]))

print('\nprint a slice,from the 4th the end (but not the last item):')
print(colors[-4:-1])

create_divider('reverse and sort the list',1,"*")

colors.reverse()
print(colors)

colors.sort()
print(colors)

create_divider('treat the list like a queue',1,"*")
print(colors)
color=colors.pop(0)
print('popped',color)

print(colors)

create_divider('add and remove elements from a list',1,"*")

print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)

create_divider('conbine a new list with an existing list',1,"*")

new_colors=['lime','gray']
colors.extend(new_colors)
print(colors)

create_divider('clear all items from a list',1,"*")
print(colors)
colors.clear()
print(colors)


#Access individual elements inside the list by using square brackets and a zero-based index. 
#Access the first item in the list by using index 0. 
#Access the last item in the list by using index -1. 
#Access items relative to the end of the list by using other negative numbers as indexes.
#Create slices by using square brackets and a colon. The colon separates the beginning of the slice, on the left, from the end of the slice, on the right.