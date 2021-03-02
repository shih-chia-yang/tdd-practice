from argparse import ArgumentParser

"""get content and count word , line ,char"""
class GetContent:
    def __init__(self,path) :
        self.word_count=0
        self.char_count=0
        self.line_count=0
        self.file_path=path
        self.max_line_length=0
        self.result_list={}
        pass

    def count(self):
        self.get_content(self.line_func)
        self.get_content(self.word_func)
        self.get_content(self.char_func)
        # self.max_line_length=4

    def get_content(self,func):
        with open(self.file_path) as content:
            lines=content.read().split("\n")
            for line in lines:
                func(line)
        line_result=f'this file {self.file_path} has lines count :{self.line_count}'
        word_result=f'this file {self.file_path} has lines count :{self.word_count}'
        char_result=f'this file {self.file_path} has lines count :{self.char_count}'
        self.result_list.update({"line_func":line_result})
        self.result_list.update({"word_func":word_result})
        self.result_list.update({"char_func":char_result})
    
    def line_func(self,line):
        self.line_count+=1

    def word_func(self,line):
        self.word_count+=len(line.split())
    
    def char_func(self,line):
        target_line=len(line)
        if target_line>self.max_line_length:
            self.max_line_length=target_line
        self.char_count+=target_line


def main():
    
    parser=ArgumentParser()
    parser.add_argument("intput_file",type=str,help="read data from this file")
    parser.add_argument("-l","--line",action="store_true",dest="line_func",default=False,help="show this file how many lines count")
    parser.add_argument("-w","--word",action="store_true",dest="word_func",default=False,help="show this file how many words count")
    parser.add_argument("-c","--char",action="store_true",dest="char_func",default=False,help="show this file how many chars count")
    args=parser.parse_args()
    getcontent=GetContent(args.__dict__["intput_file"])
    getcontent.count()
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