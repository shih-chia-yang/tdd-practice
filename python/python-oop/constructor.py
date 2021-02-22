#constructor __init()__
#special keyword self,the keyword self refers to the object's instance

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

car=Car()
print(car.color)
print(car.make)