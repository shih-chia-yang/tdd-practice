from pathlib import Path
import re

header_list=[]
content_list={}

def get_line(path):
    file=Path(path)
    with open(file,'r') as content:
        content_list=create_content_list(content.readlines())
    return content_list

def create_content_list(lines):
    global content_list,header_list
    line_index=0
    for line in lines:
        words=transfer_words(clean_line(line))
        if line_index ==0:
            header_list=words
        else:
            content_list.setdefault(line_index)
            content_list[line_index]=words
        line_index+=1
    return content_list

def clean_line(line):
    clean_line=line.replace("\n","")
    return clean_line

def get_words(clean_line):
    return clean_line.split("|")

def transfer_words(line):
    new_words=[]
    pattern=r"\d*[.]{1}\d*"
    regexp=re.compile(pattern)
    words=get_words(line)
    for word in words:
        if isfloat(word) and  regexp.search(word):
            new_words.append(float(word))
        elif isInt(word):
            new_words.append(int(word))
        else:
            new_words.append(word)
    return new_words

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
