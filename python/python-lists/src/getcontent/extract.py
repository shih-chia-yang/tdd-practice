from string import punctuation
from . import EmptyLineError

punctuation=str.maketrans("", "","-,:?!;.")

def extract_content(line):
    if not line.strip():
        raise EmptyLineError("內容不可為空")
    lower=line.lower()
    new_line=lower.translate(punctuation)
    return new_line

def get_word(line:str):
    words=line.split()
    return "\n".join(words)+"\n"