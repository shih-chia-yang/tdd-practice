class GetContent:
    def __init__(self) :
        self.word_count=0
        self.char_count=0
        self.line_count=0
        pass

    def get_content(self,path,func):
        with open(path) as content:
            lines=content.read().split("\n")
            for line in lines:
                func(line)
    
    def line_func(self,line):
        self.line_count+=1

    def word_func(self,line):
        self.word_count+=len(line.split())
    
    def char_func(self,line):
        self.char_count+=len(line)