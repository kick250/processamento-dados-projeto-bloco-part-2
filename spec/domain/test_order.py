import test
from datetime import date
from domain.order import Order
from domain.product import Product


def order():
  return Order(
    1010,
    date(2020, 12, 23),
    [Product(10, "Iphone 12", 9999.99, None)]
  )

def test_id():
  assert order().id == 1010

def test_date():
  assert order().date.year == 2020
  assert order().date.month == 12
  assert order().date.day == 23

def test_products():
  assert len(order().products) == 1