from domain.address import Address


def test_street_name():
  street = "R. São José"
  city = "Rio de janeiro"
  state = "RJ"
  number = 90
  address = Address(street, city, state, number)

  assert address.street == street

def test_city():
  street = "R. São José"
  city = "Rio de janeiro"
  state = "RJ"
  number = 90
  address = Address(street, city, state, number)

  assert address.city == city

def test_state():
  street = "R. São José"
  city = "Rio de janeiro"
  state = "RJ"
  number = 90
  address = Address(street, city, state, number)

  assert address.state == state

def test_number():
  street = "R. São José"
  city = "Rio de janeiro"
  state = "RJ"
  number = 90
  address = Address(street, city, state, number)

  assert address.number == number

def test_full_address():
  street = "R. São José"
  city = "Rio de Janeiro"
  state = "RJ"
  number = 90
  address = Address(street, city, state, number)

  assert address.full_address == "R. São José, 90, Rio de Janeiro - RJ"