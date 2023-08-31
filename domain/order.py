class Order:
  def __init__(self, id, date, products):
    self.id = id
    self.__date = date
    self.__products = products

  @property
  def date(self):
    return self.__date

  @property
  def products(self):
    return self.__products