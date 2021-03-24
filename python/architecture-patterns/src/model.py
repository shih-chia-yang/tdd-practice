from sqlalchemy import ForeignKey, Table,Column, Integer, MetaData, String,Date
from sqlalchemy.orm import mapper,relationship
from OrderLine import OrderLine
from Batch import Batch

metadata=MetaData()

order_lines=Table(
    "order_lines",
    metadata,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('sku',String(255)),
    Column('qty',Integer,nullable=False),
    Column('orderid',String(255))
)

batches=Table(
    "batches",
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("reference",String(255)),
    Column("sku",String(255)),
    Column("_purchased_quantity",Integer,nullable=False),
    Column("eta",Date,nullable=True)
)

allocations=Table(
    "allocations",
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("orderline_id",ForeignKey("order_lines.id")),
    Column("batch_id",ForeignKey("batches.id"))
)

def start_mapper():
    lines_mapper=mapper(OrderLine,order_lines)
    mapper(Batch,
           batches,
           properties={
               "_allocations":relationship
               (
               lines_mapper,
               secondary=allocations,
               collection_class=set
               )
            }
    )