
from xxlimited import new


def append_list_by_isinstance(param):
    source_list=[]
    if isinstance(param,list) is True:
        source_list+=param
    else:
        raise TypeError("型別錯誤",f'vlaue type is {type(param)}')
    return source_list

def append_list_by_type(param):
    source_list=[]
    if type(param) is type([]):
        source_list+=param
    else:
        raise TypeError("型別錯誤",f'vlaue type is {type(param)}')
    return source_list