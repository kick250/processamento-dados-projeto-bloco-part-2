class Address:
  def __init__(self, street, city, state, number):
    self.__street = street
    self.__city = city
    self.__state = state
    self.__number = number

  @property
  def street(self):
    return self.__street

  @property
  def city(self):
    return self.__city

  @property
  def state(self):
    return self.__state

  @property
  def number(self):
    return self.__number

  @property
  def full_address(self):
    return f"{self.street}, {self.number}, {self.city} - {self.state}"