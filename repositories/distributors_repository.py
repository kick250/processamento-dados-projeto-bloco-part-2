from exceptions.distributor_not_found import DistributorNotFound
from repositories.repository import Repository
from domain.distributor import Distributor
from domain.address import Address
from random import randint


class DistributorsRepository(Repository):
  __all_distributors = [
    Distributor(1, "Lojas americanas", Address("R. São José", "Rio de janeiro", "RJ", 90)),
    Distributor(4, "Lojas teste", Address("Ladeira da gloria", "Rio de janeiro", "RJ", 26))
  ]

  @classmethod
  def build(cls):
    return cls()

  def get_all(self):
    return DistributorsRepository.__all_distributors

  def get_by_id(self, id):
    distributors = self.get_all()
    for distributor in distributors:
      if distributor.id == id: return distributor

    raise DistributorNotFound()

  def create(self, distributor):
    distributor.id = randint(10, 99)
    DistributorsRepository.__all_distributors.append(distributor)

  def delete_by_id(self, id):
    print(f"Deletando id {id}")