class GetContent:
    def __init__(self) :
        self.word_count=0
        self.char_count=0
        self.line_count=0
        pass

    def get_content(self,path):
        with open(path) as content:
            lines=content.read().split("\n")
            self.line_count=len(lines)
            self.word_count=sum([len(line.split()) for line in lines])
            self.char_count=sum(len(line) for line in lines)