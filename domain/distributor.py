class Distributor:
  def __init__(self, id, name):
    self.__id = id
    self.__name = name

  @property
  def name(self):
    return self.__name