import pytest
import datetime
import sys
sys.path.append("../src")
from Batch import Batch
from OrderLine import OrderLine

def fake_can_allocate_batch_list():
        return [(fake_batch_and_line("desk", 20, 2),True),
            (fake_batch_and_line("chair", 2, 10),False),
            (fake_batch_and_line("elegant-lamp",5,5),True)]

def fake_batch_and_line(sku,batch_qty,line_qty,line_sku=""):
    if  bool(line_sku) is False:
        line_sku=sku
    batch=Batch("batch-001",sku,batch_qty,eta=datetime.date.today)
    line=OrderLine("order-001",line_sku,line_qty)
    return (batch,line)

def test_allocating_to_a_batch_reduces_the_available_quantity():
    fake_batch_qty=20
    fake_line_qty=2
    batch ,line = fake_batch_and_line("small-table",fake_batch_qty,fake_line_qty)
    batch.allocate(line)
    assert batch.available_quantity==(fake_batch_qty-fake_line_qty)

def test_can_allocate_if_available_greater_than_required():
    for actual,expected in fake_can_allocate_batch_list():
        batch,line=actual
        assert batch.can_allocate(line) is expected

def test_can_not_allocate_if_skus_do_not_match():
    batch,line =fake_batch_and_line("table",10,5,"chair")
    assert batch.can_allocate(line) is False

# def main():
#     test_allocating_to_a_batch_reduces_the_available_quantity()

# if __name__=="__main__":
#     main()