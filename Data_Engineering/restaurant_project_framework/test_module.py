# Import Table class
from restaurant import Table
# Import unittest or PyTest - Framework assumes unittest but feel free to use either
import pytest


# Write your tests here (assumes unittest is being used. Can use PyTest if you prefer)

def test_order():
    t = Table(4)
    t.order("pizza", 12, 1)
    assert t.bill[0] == {"item": "pizza", "price": 12, "quantity": 1}


def test_order_no_quantity():
    t = Table(4)
    t.order("pizza", 12)
    assert t.bill[0] == {"item": "pizza", "price": 12, "quantity": 1}


def test_remove():
    t = Table(4)
    t.order("pizza", 12)
    assert t.remove("pizza", 12) is True


def test_remove_no_item():
    t = Table(4)
    t.order("pizza", 12)
    assert t.remove("steak", 15) is False


def test_get_subtotal():
    t = Table(4)
    t.order("pizza", 12)
    t.order("steak", 15, 2)
    t.order("burger", 9, 3)
    assert t.get_subtotal() == 69


def test_get_total():
    t = Table(4)
    t.order("pizza", 12)
    t.order("steak", 15, 2)
    t.order("burger", 9, 3)
    assert t.get_total() == {"Sub Total": "£69.00", "Service Charge": f"£6.90", "Total": "£75.90"}


def test_split_bill():
    t = Table(4)
    t.order("pizza", 12)
    t.order("steak", 15, 2)
    t.order("burger", 9, 3)
    assert t.split_bill() == 17.25
