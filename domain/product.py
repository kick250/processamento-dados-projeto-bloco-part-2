class Product:
  def __init__(self, id, name, price, distributor):
    self.__id = id
    self.__name = name
    self.__price = price
    self.__distributor = distributor

  @property
  def id(self):
    return self.__id

  @property
  def name(self):
    return self.__name

  @property
  def price(self):
    return self.__price

  @property
  def distributor_id(self):
    return self.__distributor.id