import helper
from domain.address import Address
from domain.distributor import Distributor
from repositories.distributors_repository import DistributorsRepository


class CreateDistributor:
  @classmethod
  def build(cls):
    return cls(DistributorsRepository.build())

  def __init__(self, all_distributors):
    self.__all_distributors = all_distributors

  def execute(self):
    print("Novo Distribuidor")
    distributor_name = helper.read_string("Digite o nome do distribuidor: ", empty_valid=False)
    print("Endereço")
    street_name = helper.read_string("Digite o nome da rua: ", empty_valid=False)
    city = helper.read_string("Digite a cidade: ", empty_valid=False)
    state = helper.read_string("Digite o estado: ", empty_valid=False)
    number = helper.read_int("Digete o numero do endereço: ", positive = True)

    address = Address(street_name, city, state, number)
    distributor = Distributor(None, distributor_name, address)
    self.__all_distributors.create(distributor)