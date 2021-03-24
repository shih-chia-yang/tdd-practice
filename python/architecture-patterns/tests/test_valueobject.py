from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple
import pytest

@dataclass
class Name:
    first_name:str
    surname:str

class Money(NamedTuple):
    currency:str
    value:int

Line=namedtuple('Line',['sku','qty'])

class Person:
    def __init__(self,name:Name) -> None:
        self.name=name

five=Money('Dollar',5)
ten=Money('Dollar',10)

def test_equality():
    assert Money('Dollar',10)==Money('Dollar',10)
    assert Name('test1','py')==Name('test1','py')
    assert Line('chair',5)==Line('chair',5)
    
def can_add_Money_values_for_the_same_currency():
    assert five+five is ten

def can_subtract_money_values():
    assert ten-five is five

def adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money("USD",5)+Money("NT",5)

def can_multiply_money_by_a_number():
    assert five*5 is Money('Dollar',25)
    
def multiplying_two_money_values_is_an_error():
    with pytest.raises(ValueError):
        five*ten
        
def test_name_equality():
    assert Name('harry','percival')!=Name('barry','percival')

def test_person_equality():
    harry=Person(Name('harry','percival'))
    barry=harry
    barry.name=Name('barry','percival')
    assert harry is barry and barry is harry