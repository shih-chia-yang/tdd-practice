import re

def specific_number_range(value):
    pattern=r"^-?\b[0-5]{1,1}\b"
    matchs=re.match(pattern,value)
    return matchs!=None

def Hexadecimal(value):
    pattern=r"^[0-9A-Fa-f]+$"
    matchs=re.match(pattern,value)
    return matchs!=None