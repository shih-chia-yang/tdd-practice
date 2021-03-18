import sys
from pathlib import Path
import getcontent

def main():
    file_path= Path("../tests/word_count.txt")
    with open(file_path,'r') as file:
        for line in file.readlines():
            words=getcontent.get_word(getcontent.extract_content(line))
            print(words)
            num1,num2=getcontent.calculate(getcontent.word_count(words))
            print(num1,num2)

if __name__ == '__main__':
    main()
    