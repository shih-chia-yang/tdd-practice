from pathlib import Path
import re

header_list=[]
content_list={}

def get_line(path):
    file=Path(path)
    global content_list,header_list
    line_count=0
    with open(file,'r') as content:
        for line in content.readlines():
            clean_line=line.replace("\n","")
            words=get_words(clean_line.split("|"))
            if line_count ==0:
                header_list=words
            else:
                content_list.setdefault(line_count)
                content_list[line_count]=words
            line_count+=1
    return content_list

def get_words(line):
    words=[]
    pattern=r"\d*[.]{1}\d*"
    regexp=re.compile(pattern)
    for word in line:
        if isfloat(word) and  regexp.search(word):
            words.append(float(word))
        elif isInt(word):
            words.append(int(word))
        else:
            words.append(word)
    return words

def isfloat(value):
    try:
        float(value)
        return True 
    except ValueError:
        return False

def isInt(value):
    try:
        int(value)
        return True 
    except ValueError:
        return False
