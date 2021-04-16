def process_numbers(arglist):
    numbers=[]
    if isinstance(arglist,list)==False:
        return numbers
    for arg in arglist:
        if isinstance(arg,int):
            numbers.append(arg)
        elif isinstance(arg,str):
            if arg.isnumeric():
                numbers.append(int(arg))
    numbers.sort()
    return numbers


def process_names(arglist):
    strs=[]
    if isinstance(arglist,list)==False:
        return strs
    for arg in arglist:
        if isinstance(arg,str):
            if arg.isnumeric()==False:
                strs.append(arg)

    strs.sort()
    return strs