
from typing import List
from Batch import Batch
from OrderLine import OrderLine
from OutOfStock import OutOfStock

def allocate(line: OrderLine,batches: List[Batch]) -> str:
    #sorted_batch=sorted(batches,key= lambda batch:batch.eta)
    try:
        sorted_batch=sorted(batches)
        batch=next(batch for batch in sorted_batch if batch.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"out of stock for sku {line.sku}")
        