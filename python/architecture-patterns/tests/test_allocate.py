import datetime
import pytest
import references
from Batch import Batch
from OrderLine import OrderLine
from allocate import allocate
from OutOfStock import OutOfStock

tomorrow=datetime.date.today() + datetime.timedelta(days=1)
today=datetime.date.today()
later=datetime.date.today() + datetime.timedelta(days=2)

def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch=Batch('in-stock-batch',"clock",100,eta=None)
    shipment_batch=Batch('sheipment-bath','clock',100,eta=tomorrow)
    line=OrderLine('oref','clock',10)
    allocation=allocate(line,[in_stock_batch,shipment_batch])
    assert in_stock_batch.available_quantity==90
    assert shipment_batch.available_quantity==100
    assert allocation ==in_stock_batch.reference
    
def test_prefers_earlier_batches():
    earlist=Batch("speedy-batch","spoon",100,eta=today)
    medium=Batch("normal-batch","spoon",100,eta=tomorrow)
    latest=Batch("slow-batch","spoon",100,eta=later)
    line=OrderLine("order1","spoon",10)
    allocate(line,[medium,earlist,latest])
    assert earlist.available_quantity==90
    assert medium.available_quantity==100
    assert latest.available_quantity==100

def test_raises_out_of_stock_exception_if_can_not_allocate():
    batch=Batch('batch1',"desk",10,eta=today)
    allocate(OrderLine('order1','desk',10),[batch])
    with pytest.raises(OutOfStock,match='desk'):
        allocate(OrderLine('order2','desk',2),[batch])