from pathlib import Path
import re
#"hello|Hello"  | =or
#(h|H)ello 
#[hH]ello   []特殊字元，代表中間的字元任選一個
#[a-z] 代表a到z之間的任一字元
#re module document https://docs.python.org/3/library/re.html
# pythex.org  regex測試工具網站
regexp=re.compile("[hH]ello")
lines=[]
file_path=Path("./tests/sample.txt")
with open(file_path,'r') as sample:
    lines=[line for line in sample.readlines() if regexp.search(line)]
print(len(lines))