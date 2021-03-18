
phone_book={"123":"45672321","test2":"93475462983","test2":"232134343"}
def serach_value(string):
    try:
        global phone
        phone=phone_book.get(string)
    except KeyError:
        phone= None
    finally:
        return phone

print(serach_value('6676'))

class ValueToLarge(Exception):
    pass

x=1001
if x>1000:
    raise ValueToLarge("error","超過1000",f'value :{x}',3)