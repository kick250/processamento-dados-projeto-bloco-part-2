import test
from domain.product import Product
from domain.distributor import Distributor

def create_product():
  id = 10
  name = "Carlos"
  price = 99.99
  distributor = Distributor(1, "Lojas americanas", None)
  return Product(id, name, price, distributor)

def test_id():
  assert create_product().id == 10

def test_name():
  assert create_product().name == "Carlos"

def test_price():
  assert create_product().price == 99.99

def test_distributor_id():
  assert create_product().distributor_id == 1

def test_distributor_name():
  assert create_product().distributor_name == "Lojas americanas"