import re

def extract_number(phone):
    pattern=r"(?P<phone>(\+\d{1,3}-)?(\d{3}-)?\d{3}-\d{4})"
    matchs=re.match(pattern,phone)
    return matchs!=None