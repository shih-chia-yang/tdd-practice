import pytest
import datetime
import sys
sys.path.append("../src")
from Batch import Batch
from OrderLine import OrderLine

def fake_can_allocate_batch_list():
        return [("desk", 20, 2,True),
            ("chair", 2, 10,False)]

def fake_batch_and_line(sku,batch_qty,line_qty):
    return (Batch("batch-001",sku,batch_qty,eta=datetime.date.today),
            OrderLine("order-001",sku,line_qty))

def test_allocating_to_a_batch_reduces_the_available_quantity():
    fake_batch_qty=20
    fake_line_qty=2
    batch ,line = fake_batch_and_line("small-table",fake_batch_qty,fake_line_qty)
    batch.allocate(line)
    assert batch.available_quantity==(fake_batch_qty-fake_line_qty)

def test_can_allocate_if_available_greater_than_required():
    for sku,batch_qty,line_qty,expected in fake_can_allocate_batch_list():
        batch ,line = fake_batch_and_line(sku,batch_qty,line_qty)
        assert batch.can_allocate(line) is expected
# def main():
#     test_allocating_to_a_batch_reduces_the_available_quantity()

# if __name__=="__main__":
#     main()