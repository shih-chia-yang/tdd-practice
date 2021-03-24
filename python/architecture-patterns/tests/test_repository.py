from Batch import Batch
from OrderLine import OrderLine
from repository import BatchRepository

    
def test_repository_can_save_batch(session):
    batch=Batch("batch1","soapdish",100,eta=None)
    repo=BatchRepository(session)
    repo.add(batch)
    session.commit()
    
    rows=session.execute(
        'select reference ,sku,_purchased_quantity,eta from batches'
    )
    
    assert list(rows)==[(batch.reference
                         ,batch.sku
                         ,batch._purchased_quantity
                         ,batch.eta)]
    
def insert_order_line(session):
    session.execute(" insert into order_lines (orderid,sku,qty)" 
                    'values ("order1","sofa",12)')
    
    [[order_line_id]]=session.execute(
    "select id from order_lines where orderid=:orderid and sku=:sku",
    dict(orderid="order1",sku="sofa"))
    
    return order_line_id

def insert_batch(session,batch_id):
    session.execute(
        "insert into batches (reference,sku,_purchased_quantity,eta)"
        'values (:batch_id,"sofa",100,null)',
        dict(batch_id=batch_id)
    )
    
    [[batch_id]]=session.execute(
        'select id from batches where reference=:batch_id and sku="sofa"',
        dict(batch_id=batch_id)
    )
    return batch_id

def insert_allocation(session,orderline_id,batch_id):
    session.execute(
        "insert into allocations (orderline_id,batch_id)"
        'values (:orderline_id,:batch_id)',
        dict(orderline_id=orderline_id,batch_id=batch_id)
    )

def test_repository_can_retrieve_a_batch_with_allocation(session):
    orderline_id=insert_order_line(session)
    batch1_id=insert_batch(session,"batch1")
    insert_batch(session,"batch2")
    insert_allocation(session,orderline_id,batch1_id)
    
    repo=BatchRepository(session)
    retrieved=repo.get("batch1")
    expected=Batch("batch1","sofa",100,eta=None)
    assert retrieved==expected
    assert retrieved.sku==expected.sku
    assert retrieved._purchased_quantity==expected._purchased_quantity
    assert retrieved._allocations=={
        OrderLine("order1","sofa",12)
    }