# print()

def exiting():
    return ['Exiting']

def complete():
    return ['Continuing...','Complete!']

def Merge(dict1, dict2):
    return(dict2.update(dict1))

ans=input('Would you like to continue?')
dict1={item:complete() for item in ["yes","y"]}
dict2={item:exiting() for item in ["no","n"]}

Merge(dict1, dict2)
# func_dict={"no":exiting(),"n":exiting(),"yes":complete(),"y":complete()}
messages=dict2[ans]
for message in messages:
    print(message)

# python 沒有switch-case
# 可使用 
# def do_a_stuff():
# def do_b_stuff():
# def do_c_stuff():
# func_dict={"a":do_a_stuff(),"b":do_b_stuff(),"c":do_c_stuff()}
# x='a'
# func_dict[x]()