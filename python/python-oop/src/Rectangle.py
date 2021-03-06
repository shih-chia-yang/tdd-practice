class Rectangle:
    def __init__(self,h,w):
        self.height=h
        self.width=w
        pass

    def area(self):
        return self.height*self.width


a = Rectangle(5,6)
print(a.area())

b=Rectangle(5,4)
print(b.area())