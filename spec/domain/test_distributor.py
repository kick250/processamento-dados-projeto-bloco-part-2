from domain.distributor import Distributor
from domain.address import Address


def test_name():
  address = Address("R. São José", "Rio de janeiro", "RJ", 90)
  expected_name = "Carlos distribuidor"
  distributor = Distributor(1, expected_name, address)

  assert distributor.name == expected_name
  assert distributor.id == 1

def test_full_address():
  address = Address("R. São José", "Rio de janeiro", "RJ", 90)
  expected_name = "Carlos distribuidor"
  distributor = Distributor(1, expected_name, address)

  assert distributor.full_address == "R. São José, 90, Rio de Janeiro - RJ"