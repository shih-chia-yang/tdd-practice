# constructor __init()__
# special keyword self,the keyword self refers to the object's instance
# If you need to be reminded how to model, see the section "Find objects, data, and behavior" in the second unit. 
# Remember, modeling starts with asking the questions who interacts with whom or who does what to whom.
#
#python 命名慣例
#一般變數與函式都是全部英文小寫(偶爾加上底線)
#類別的命名是每個英文單字的第一個字母都大寫

#python變數隨時都可以建立，物件裡的變數也可以不用事先在class裡定義
#物件名.變數名=變數值

class Circle:
    """a empty class"""
    pass
#無宣告任何變數

my_circle1=Circle()
my_circle1.radius=5
print(2*3.14*my_circle1.radius)

my_circle2=Circle()
my_circle2.radius=3
print(2*3.14*my_circle2.radius)

#__doc__可以用來取得文件字串的內容

print(my_circle1.__doc__)

class Elevator:
    #__init__初始化物件的變數，類似java的建構子(constructor)
    # python class只能有一個__init__，與java和c++不同
    def __init__(self,starting_floor):
        self.make="the elevator company"
        self.floor=starting_floor

elevator =Elevator(1)
print(elevator.make)
print(elevator.floor)

class Car:
    def __init__(self):
        self.color="red"
        #self.make為物件變數
        self.make="mercedes"
        # make為區域變數
        make="123"
    def run(self):
        return 0

car=Car()
print(car.color)
print(car.make)
print(car.run())

symbol=['rock','paper','scissor']
print('rock' in symbol)


# protect your data
# having two leading underscores ,__,which is referred to as private
# self.__name
# not entirely safe.Python just changes the name of the underlying data
# square=Square()
# square._Square__height=3 ,is allowed
# Python is unique in that data protection is more like levels of suggestion rather than being strictly implemented.

class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(new_side):
      self.__height = new_side
      self.__width = new_side

square = Square()
square._Square__height = 3 # is allowed

#Use decorators for getters and setters
class Square:
    def __init__(self, w, h):
        self.height = h
        self.__width = w
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Value must be larger than 0")

square = Square(1,2)
square.__height=3
print(square.height)
square.height=3
print(square.height)
square._Square__height=4
print(square.height)
