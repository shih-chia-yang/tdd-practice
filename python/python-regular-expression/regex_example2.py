import re
from pathlib import  Path

regexp=re.compile(r"(?P<last>[-a-zA-Z]+),"
                               r" (?P<first>[-a-z-A-Z]+)"
                               r"( (?P<middle>[a-z-A-Z]+))?"
                               r": (?P<phone>(\d{3}-)?\d{3}-\d{4})")

file_path=Path("./tests/textfile.txt")
with open(file_path,'r') as file:
    for line in file.readlines():
        result= regexp.search(line)
        if result ==  None:
            print("can't found anything")
        else:
            last_name=result.group('last')
            first_name=result.group('first')
            middle_name=result.group('middle')
            if middle_name==None:
                middle_name=""
            phone_number=result.group('phone')
        print('Name :',first_name,middle_name,last_name,'Number:',phone_number)
            