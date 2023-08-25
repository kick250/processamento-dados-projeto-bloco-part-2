from domain.distributor import Distributor

def test_name():
  expected_name = "Carlos distribuidor"
  distributor = Distributor(1, expected_name)

  assert distributor.name == expected_name