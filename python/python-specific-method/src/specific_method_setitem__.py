#__setitem__
#使用object[n]=value的形式以索引賦值

class MyList:
    def __init__(self,length):
        self.list=[None]*length
    
    def __getitem__(self,index):
        if index>=len(self.list):
            raise IndexError
        return self.list[index]
    
    def __setitem__(self,index,value):
        self.list[index]=value


c=MyList(4)
print(list(c))
c[1]="one"
print(c[1])
print(list(c))