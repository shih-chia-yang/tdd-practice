# some-notes-on-allocation

- SKU : stock-keeping unit

customers place orders. an order is identified by an order reference and comprises multiple order lines,
where each line has a SKU and a quantity.

- 10 units of read-chair
- 1 unit of tasteless-lamp

## rules

1.  the available quantity is reduced by x 

- [x] we have a batch of 20 small-table, and we allocate an order line for 2 small-table.

- [x] the batch should have 18 small-table remaining

2.  can't allocate to a batch if the available quantity is less than the quantity of the order line

- [x]  we have a batch of 1 blue-cushion, and an order line for 2 blue-cushion

- [x] we should not be able to allocate the line to the batch

3. can't allocate the same line twice

- we have a batch of 10 blue-vase, and we allocate an order line for 2 blue-vase

- if we allocate the order line again to the same batch, the batch should still have an available quantity of 8

