from exceptions.distributors_do_not_exist_exception import DistributorsDoNotExistException
from repositories.distributors_repository import DistributorsRepository
from repositories.products_repository import ProductsRepository
import helper
from domain.product import Product


class CreateProduct:
  @classmethod
  def build(cls):
    return cls(ProductsRepository.build(), DistributorsRepository.build())

  def __init__(self, all_products, all_distributors):
    self.__all_products = all_products
    self.__all_distributors = all_distributors

  def execute(self):
    try:
      print("Produto")
      name = helper.read_string("Digite o nome: ", empty_valid=False)
      price = helper.read_float("Digite o preço: ", positive=True)
      distributor = self.__ask_for_distributor()
      product = Product(None, name, price, distributor)
      self.__all_products.create(product)
    except DistributorsDoNotExistException as e:
      print(str(e))

  def __ask_for_distributor(self):
    print("Selecione o distribuidor: ")
    distributors = self.__all_distributors.get_all()

    if len(distributors) == 0: raise DistributorsDoNotExistException()

    for distributor in distributors:
      print(f'{distributor.id} {distributor.name}')
    distributors_ids = tuple(map(lambda x: x.id, distributors))

    distributor_id = helper.read_int("Distribuidor: ", options=distributors_ids)
    return self.__all_distributors.get_by_id(distributor_id)
