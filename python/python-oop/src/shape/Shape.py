class Shape:
    def __init__(self,_x,_y):
        self.x=_x
        self.y=_y
    
    def move(self,delta_x,delta_y):
        self.x=self.x+delta_x
        self.y=self.y+delta_y