from pathlib import Path
from string import punctuation 

punctuation=str.maketrans("", "","-,:?!;.")

def get_word(path):
    file_path=Path(path)
    with open(file_path,'r') as file:
        for line in file.read().split("\n\n"):
            contents=line.lower().translate(punctuation).split()
    return contents