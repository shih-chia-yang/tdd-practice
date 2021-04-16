import re
import clean

def transfer_words(line):
    new_words=[]
    pattern=r"\d*[.]{1}\d*"
    regexp=re.compile(pattern)
    words=clean.get_words(line)
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