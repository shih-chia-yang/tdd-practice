# constructor __init()__
# special keyword self,the keyword self refers to the object's instance
# If you need to be reminded how to model, see the section "Find objects, data, and behavior" in the second unit. 
# Remember, modeling starts with asking the questions who interacts with whom or who does what to whom.
#

class Elevator:
    def __init__(self,starting_floor):
        self.make="the elevator company"
        self.floor=starting_floor

elevator =Elevator(1)
print(elevator.make)
print(elevator.floor)

class Car:
    def __init__(self):
        self.color="red"
        self.make="mercedes"
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
