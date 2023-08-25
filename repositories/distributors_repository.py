from exceptions.distributor_not_found import DistributorNotFound
from repositories.repository import Repository
from domain.distributor import Distributor
from domain.address import Address

class DistributorsRepository(Repository):
  def get_all(self):
    results = self._execute("SELECT * FROM distributors JOIN addresses ON addresses.distributor_id = distributors.id")
    return tuple(map(self.__create_distributor, results))

  def get_by_id(self, id):
    results = self._execute(f"SELECT * FROM distributors JOIN addresses ON addresses.distributor_id = distributors.id WHERE distributors.id = {id}")

    if len(results) == 0: raise DistributorNotFound()

    return self.__create_distributor(results[0])

  def create(self, distributor):
    pass #

  def delete_by_id(self, id):
    pass #

  def __create_distributor(self, row):
    id = row[0]
    name = row[1]
    street = row[2]
    city = row[3]
    state = row[4]
    number = row[5]
    return Distributor(id, name, Address(street, city, state, number))