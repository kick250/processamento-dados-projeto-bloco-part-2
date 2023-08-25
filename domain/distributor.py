class Distributor:
  def __init__(self, id, name, address):
    self.__id = id
    self.__name = name
    self.__address = address

  @property
  def id(self):
    return self.__id

  @property
  def name(self):
    return self.__name

  @property
  def full_address(self):
    return self.__address.full_address