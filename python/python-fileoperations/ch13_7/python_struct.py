import struct,sys


record_format='hd4s'
record_size=struct.calcsize(record_format)
content=struct.pack(record_format,7,3.14,b'gbye')
print(content)
unpack_content=struct.unpack(record_format,content)
print (unpack_content)
print(unpack_content==(7,3.14,b'gbye'))
result_list=[]
# with open("data",'w') as data:
#     content=struct.pack(record_format,7,3.14,b'gbye')
#     sys.stdout=data
#     sys.stdout.buffer.write(content)


with open("data",'rb')  as read_data:
    while 1:
        record=read_data.read()
        if record is False:
            break;
        result_list.append(struct.unpack(record_format,record))
    
    