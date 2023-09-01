from repositories.distributors_repository import DistributorsRepository
import helper


class DeleteDistributor:
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

    if len(distributors) == 0: return print("Não existem distribuidores")

    for distributor in distributors:
      print(f'{distributor.id} {distributor.name}')
    distributors_ids = tuple(map(lambda x: x.id, distributors))

    distributor_id = helper.read_int("Qual distribuidor voce deseja deletar: ", options=distributors_ids)
    self.__all_distributor.delete_by_id(distributor_id)