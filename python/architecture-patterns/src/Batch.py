from datetime import date
from typing import Optional
from OrderLine import OrderLine

class Batch():

    def __init__(self,ref:str,sku:str,qty:int,eta:Optional[date]):
        self.reference=ref
        self.sku=sku
        self.eta=eta
        self._purchased_quantity=qty
        self._allocations=set()
        
    @property
    def allocated_quantity(self)->int:
        return sum( line.qty for line in self._allocations)
        
    @property
    def available_quantity(self)->int:
        return self._purchased_quantity-self.allocated_quantity
    
    def allocate(self,line:OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)
    
    def deallocate(self,line:OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)
        
    def can_allocate(self,line:OrderLine)->bool:
        return self.sku==line.sku and self.available_quantity>=line.qty
        