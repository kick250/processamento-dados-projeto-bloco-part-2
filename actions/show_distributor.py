from repositories.distributors_repository import DistributorsRepository
import helper


class ShowDistributor:
  @classmethod
  def build(cls):
    return cls(
      DistributorsRepository.build()
    )

  def __init__(self, all_distributor):
    self.__all_distributor = all_distributor

  def execute(self):
    print("Distribuidores:")
    distributors = self.__all_distributor.get_all()
    for distributor in distributors:
      print(f'{distributor.id} {distributor.name}')
    distributors_ids = tuple(map(lambda x: x.id, distributors))

    distributor_id = helper.read_int("Qual distribuidor voce deseja ver: ", options=distributors_ids)
    distributor = self.__all_distributor.get_by_id(distributor_id)

    print(f"Id: {distributor.id}")
    print(f"Nome: {distributor.name}")
    print(f"Endereço: {distributor.full_address}")