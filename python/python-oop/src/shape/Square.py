from Shape import Shape

class Square(Shape): #<---表示Square繼承自Shapr
    def __init__(self,_side=1,_x=0,_y=0):
        super().__init__(_x,_y)#<--繼承時必須先呼叫父類別的__init__方法
        self.side=_side#<--再進行屬於自己的複始化動作