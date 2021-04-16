first_string='A literal string'
second_string='A literal string'
print(second_string==first_string)

third_string='A single quoted literal string with a "double quote'
fourth_string="A double quoted literal string with a ' single quote"
fifth_string='A single quoted literal strng with an \' excaped single quote'
sixth_string="A double  quoted literal string with a \" double quote"
seventh_string='A literal string with a \n new line character'
eighth_string='A literal string with a \t tab character'

print(third_string)
print(fourth_string)
print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

ninth_string=r"A liter string with a \n new line character printed raw"
print(ninth_string)


tentth_string='''A literal string
on more than one line
sometimes known as a verbatim string'''

elevnth_string ="""Another literal string
    on more than one line
using double quotes"""

print(tentth_string)
print(elevnth_string)

first='Conrad'
second='Grant'
third='Bob'

print(first,second)
print(first,second,third)
print(first,second,third,sep='-')
print(first,second,third,sep='-',end='.')

# \'

print('\'')
# \"
print('\"')
# \\
print('\\')
# \a
print('\a')
# \b
print('\b')
# \f
print('\f')
# \n
print('\n')
# \r
print('1234\r\n1234')
# \t
print('\t')
# \v
print('\v')


