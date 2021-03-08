import pathlib
#__getitem__
#如果類別中定義了__getitem()__，則該類別就可以用for來巡訪
class Mylist:
    def __getitem__(self,index):
        if index>=5:
            raise IndexError
        return index

c= Mylist()
for n in c:
    print(n)

class LineReader:
    def __init__(self,path):
        self._path=path
        self.fileobject=open(self._path,'r')
    
    def __getitem__(self,index):
        line=self.fileobject.readline()
        if line =="":
            self.fileobject.close()
            raise IndexError
        else:
            return line.split("::")[:2]

orders=LineReader(pathlib.Path("../tests/sample.txt"))
for name ,age in orders:
    print(name,age)

try:
    print(orders[1:2])
except Exception as ex:
    print("發生錯誤",ex)