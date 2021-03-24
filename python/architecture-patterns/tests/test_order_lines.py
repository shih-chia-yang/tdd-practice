from OrderLine import OrderLine

def test_order_lines_mapper_can_load_lines(session):
    session.execute("insert into order_lines (orderid,sku,qty) values"
                    '("order1","chair",12),'
                    '("order2","table",13),'
                    '("order3","lipstick",14)'
                    )
    expected=[OrderLine('order1','chair',12),
              OrderLine('order2','table',13),
              OrderLine('order3','lipstick',14),]
    
    assert session.query(OrderLine).all()==expected
    
def test_orderline_mapper_can_svae_lines(session):
    new_line=OrderLine("order1","widget",12)
    session.add(new_line)
    session.commit()
    
    rows=list(session.execute('select orderid,sku,qty from order_lines'))
    assert rows ==[(new_line.orderid,new_line.sku,new_line.qty)]