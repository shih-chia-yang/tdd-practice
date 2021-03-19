from datetime import date
from typing import Optional
from OrderLine import OrderLine

class Batch():
    def __init__(self,ref:str,sku:str,qty:int,eta:Optional[date]):
        self.reference=ref
        self.sku=sku
        self.available_quantity=qty
        self.eta=eta
    
    def allocate(self,line:OrderLine):
        self.available_quantity-=line.qty
        