import pytest
import datetime

def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("small-table",quantity=20,eta=datetime.date.today)
    line=OrderLine("order1","small-table",2)
    batch.allocate(line)
    assert batch.available_quantity==18

def main():
    test_allocating_to_a_batch_reduces_the_available_quantity()

if __name__=="__main__":
    main()