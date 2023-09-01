import helper
from repositories.distributors_repository import DistributorsRepository
from domain.address import Address
from domain.distributor import Distributor
from exceptions.distributors_do_not_exist_exception import DistributorsDoNotExistException


class UpdateDistributor:
  @classmethod
  def build(cls):
    return cls(DistributorsRepository.build())

  def __init__(self, all_distributors):
    self.__all_distributors = all_distributors

  def execute(self):
    try:
      distributor_id = self.__get_distributor_id()

      distributor = self.__read_distributor()
      distributor.id = distributor_id

      self.__all_distributors.update(distributor)
    except DistributorsDoNotExistException as e:
      print(str(e))

  def __read_distributor(self):
    print("Editar Distribuidor")
    distributor_name = helper.read_string("Digite o nome do distribuidor: ", empty_valid=False)
    print("Endereço")
    street_name = helper.read_string("Digite o nome da rua: ", empty_valid=False)
    city = helper.read_string("Digite a cidade: ", empty_valid=False)
    state = helper.read_string("Digite o estado: ", empty_valid=False)
    number = helper.read_int("Digete o numero do endereço: ", positive = True)

    address = Address(street_name, city, state, number)
    return Distributor(None, distributor_name, address)


  def __get_distributor_id(self):
    print("Distribuidores:")
    distributors = self.__all_distributors.get_all()

    if len(distributors) == 0: raise DistributorsDoNotExistException()

    for distributor in distributors:
      print(f'{distributor.id} {distributor.name}')
    distributors_ids = tuple(map(lambda x: x.id, distributors))

    return helper.read_int("Qual distribuidor voce deseja editar: ", options=distributors_ids)