class Rectangle:
    def __init__(self,h,w):
        self.__height=h
        self.__width=w

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self,_h):
        if(_h>0):
            self.__height=_h
        else:
            raise ValueError("height不可為負數",f'value :{_h}')
    
    @width.setter
    def width(self,_w):
        if(_w>0):
            self.__width=_w
        else:
            raise ValueError("width不可為負數",f'value :{_w}')

    def area(self):
        return self.height*self.width


# a = Rectangle(5,6)
# print(a.area())

# b=Rectangle(5,4)
# print(b.area())