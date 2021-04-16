import struct,sys

_test_file_path="./tests/data"
record_format='hd4s'
record_size=struct.calcsize(record_format)
print (record_size)
content=struct.pack(record_format,7,3.14,b'gbye')
print(content)
unpack_content=struct.unpack(record_format,content)
print (unpack_content)
print(unpack_content==(7,3.14,b'gbye'))


result_list=[]
with open(_test_file_path,'w') as data:
    content=struct.pack(record_format,7,3.14,b'gbye')
    sys.stdout=data
    sys.stdout.buffer.write(content)


with open(_test_file_path,'rb')  as read_data:
    while True:
        record=read_data.read()
        if record =="":
            break
        else:
            result_list.append(struct.unpack(record_format,record))
            break
    
    