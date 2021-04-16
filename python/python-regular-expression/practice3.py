import re

def add_nation_number(match_object):
    return "+1-"+match_object.group('num')

def replace_number(number):
    pattern=r"(?P<num>^\d{3}-\d{3}-\d{4})$"
    regepx=re.compile(pattern)
    new_number=regepx.sub(add_nation_number,number)
    return new_number