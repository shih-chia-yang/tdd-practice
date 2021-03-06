from Shape import Shape

"""circle 模組：包含Circle類別"""
class Circle(Shape):
    """Circle類別"""
    #class variables 類別變數
    # 可用於追蹤某些類別級的資訊，例如建立了多少個物件
    # 類別建立的所有物件都可以存取
    pi=3.14159
    all_circles=[]
    def __init__(self,r=1,_x=0,_y=0):
        super().__init__(_x,_y)
        #object variables
        self.radius=r
        #area variables
        radius=2
        self.__class__.all_circles.append(self)

    #物件方法
    #定義在類別內的函式
    #物件.方法的語法被稱為綁定式方法調用(bound method invocation)
    def area(self):
        """計算面積"""
        return self.radius**2*self.__class__.pi
    
    def perimeter(self):
        """計算周長"""
        return self.radius*2*self.__class__.pi

    #類別方法
    #類似於靜態方法，但類別方法會以本身做為第一個參數傳遞
    #與物件方法會將物件本身傳遞至self參數類似
    #使用類別方法的好處在於不必將類別名稱寫死在total_area中，不必擔心更改類別名稱造成錯誤
    @classmethod
    def sum_area(cls):
        return sum([circle.area() for circle in cls.all_circles])

    @classmethod
    def total_perimeter(cls):
        return sum([ circle.perimeter() for circle in cls.all_circles])

    #靜態方法允許即時沒有建立物件也可以呼叫該類別的方法
    #使用@staticmethod修飾器
    @staticmethod
    def total_area():
        """用來計算 all_circles這個lisj所有物件的總面積的靜態方法"""
        return sum([circle.area() for circle in Circle.all_circles])

#tip
#類別變數、類別方法或靜態方法都是不用經由物件，直接可以存取的變數與方法
#可以把公用的變數和函式放在類別裡，讓各物件交換或共用
# ，也可避免相同的資料或程式在各物件都有一份而佔用記憶體


