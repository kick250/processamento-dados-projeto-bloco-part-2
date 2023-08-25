class Distributor:
  def __init__(self, id, name, address):
    self.id = id
    self.__name = name
    self.__address = address

  @property
  def name(self):
    return self.__name

  @property
  def address(self):
    return self.__address

  @property
  def full_address(self):
    return self.__address.full_address