class Product:
  def __init__(self, id, name, price, distributor):
    self.id = id
    self.__name = name
    self.__price = price
    self.__distributor = distributor

  @property
  def name(self):
    return self.__name

  @property
  def price(self):
    return self.__price

  @property
  def distributor_id(self):
    return self.__distributor.id

  @property
  def distributor_name(self):
    if self.__distributor == None: return ""

    return self.__distributor.name