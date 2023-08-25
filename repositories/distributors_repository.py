from exceptions.distributor_not_found import DistributorNotFound
from repositories.repository import Repository
from domain.distributor import Distributor
from domain.address import Address


class DistributorsRepository(Repository):
  @classmethod
  def build(cls):
    return cls()

  def get_all(self):
    return [
      Distributor(1, "Lojas americanas", Address("R. São José", "Rio de janeiro", "RJ", 90)),
      Distributor(4, "Lojas teste", Address("Ladeira da gloria", "Rio de janeiro", "RJ", 26))
    ]

  def get_by_id(self, id):
    distributors = self.get_all()
    for distributor in distributors:
      if distributor.id == id: return distributor

    raise DistributorNotFound()