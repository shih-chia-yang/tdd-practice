from argparse import ArgumentParser
import sys

"""get content and count word , line ,char"""

class Getcontent:
    def __init__(self,path) :
        self.word_count=0
        self.char_count=0
        self.line_count=0
        self.max_line_length=0
        self.file_path=path
        self.result_list={}
        pass

    def get_content(self):
        if len(self.file_path)>0:
            infile=open(self.file_path[0],'r')
        else:
            infile=sys.stdin
        for line in infile:
            line=line.replace("\n","")
            self.line_func(line)
            self.word_func(line)
            self.char_func(line)
        infile.close()
        line_result=f'this file {self.file_path} has lines count :{self.line_count}'
        word_result=f'this file {self.file_path} has words count :{self.word_count}'
        char_result=f'this file {self.file_path} has chars count :{self.char_count}'
        self.result_list.update({"line_func":line_result})
        self.result_list.update({"word_func":word_result})
        self.result_list.update({"char_func":char_result})
    
    def line_func(self,line):
        self.line_count+=1

    def word_func(self,line):
        words=line.split()
        self.word_count+=len(words)
    
    def char_func(self,line):
        target_line=len(line)
        if target_line>self.max_line_length:
            self.max_line_length=target_line
        self.char_count+=target_line


def main():
    parser=ArgumentParser()
    parser.add_argument("files",metavar='FILE',nargs='*',help="read data from this file")
    parser.add_argument("-l","--line",action="store_true",dest="line_func",default=False,help="show this file how many lines count")
    parser.add_argument("-w","--word",action="store_true",dest="word_func",default=False,help="show this file how many words count")
    parser.add_argument("-c","--char",action="store_true",dest="char_func",default=False,help="show this file how many chars count")
    args=parser.parse_args()
    getcontent=Getcontent(args.files)
    getcontent.get_content()
    show=False
    for func in args.__dict__:
        if func in getcontent.result_list and bool(args.__dict__[func]):
            print(getcontent.result_list[func])
            show=True
    if not show :
        for result in getcontent.result_list.values():
            print(result)
    

if __name__=='__main__':
    main()