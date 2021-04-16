import re

def number_formatting(number):
    pattern=r"^\+?(?P<nat>([1])?)[ -.]?[(]?(?P<area>[2-9]\d{2}?)[)]?[ -.](?P<ex>[2-9][2-8]\d{1})[ -.](?P<tail>\d{4})"
    regexp=re.compile(pattern)
    match_result=regexp.search(number)
    if match_result==None:
        raise ValueError("無效的電話號碼",f'number :{number}' )
    standatd_fotmat=regexp.sub(_replace_to_stnadard_format,number)
    return standatd_fotmat

def _replace_to_stnadard_format(match):
    nation=match.group("nat") if match.group("nat") !="" else "1"
    area=match.group("area")
    ex=match.group("ex")
    tail=match.group("tail")
    return f'{nation}-{area}-{ex}-{tail}'