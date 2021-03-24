import pytest
import datetime
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
    
def test_can_not_allocate_order_again_to_the_batch():
    batch ,order1 = fake_batch_and_line("small-table",20,2)
    order1_copy=OrderLine(order1.orderid,order1.sku,order1.qty)
    batch.allocate(order1)
    batch.allocate(order1_copy)
    assert len(batch._allocations)==1

def test_total_purchased_quantity_form_different_order_line():
    batch ,order1 = fake_batch_and_line("small-table",20,2)
    order2=OrderLine("order-002",order1.sku,order1.qty)
    batch.allocate(order1)
    batch.allocate(order2)
    assert batch.available_quantity==20-(order1.qty+order2.qty)

def test_can_only_deallocate_allocated_lines():
    batch ,order1 = fake_batch_and_line("small-table",20,2)
    batch.allocate(order1)
    batch.deallocate(order1)
    assert batch.available_quantity==20
    
    
def main():
    test_allocating_to_a_batch_reduces_the_available_quantity()

if __name__=="__main__":
    main()