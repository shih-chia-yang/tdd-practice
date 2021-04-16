import uuid
import pytest
from random import random
import requests
import config

def random_surfix():
    return uuid.uuid4().hex[:6]

def random_sku(name=''):
    return f'sku-{name}-{random_surfix()}'

def random_batch(name=''):
    return f'batch-{name}-{random_surfix()}'

def random_orderid(name=''):
    return f'order-{name}-{random_surfix()}'

@pytest.mark.usefixtures('restart_api')
def test_api_return_allocation(add_stock):
    sku,othersku=random_sku(),random_sku('other')
    earlybatch=random_batch(1)
    laterbatch=random_batch(2)
    otherbatch=random_batch(3)
    add_stock([
        (laterbatch,sku,100,'2011-01-02'),
        (earlybatch,sku,100,'2011-01-01'),
        (otherbatch,othersku,100,None)
    ])
    data={'orderid':random_orderid(),'sku':sku,'qty':3}
    url=config.get_api_url()
    request=requests.post(f'{url}/allocate',json=data)
    assert request.status_code == 201
    assert request.json()['batch']==earlybatch