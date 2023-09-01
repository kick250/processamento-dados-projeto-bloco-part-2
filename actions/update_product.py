from repositories.products_repository import ProductsRepository
from repositories.distributors_repository import DistributorsRepository
from exceptions.products_do_not_exist_exception import ProductsDoNotExistException
from exceptions.distributors_do_not_exist_exception import DistributorsDoNotExistException
from domain.product import Product
import helper


class UpdateProduct:
  @classmethod
  def build(cls):
    return cls(ProductsRepository.build(), DistributorsRepository.build())

  def __init__(self, all_products, all_distributors):
    self.__all_products = all_products
    self.__all_distributors = all_distributors

  def execute(self):
    try:
      product_id = self.__ask_product_id()

      product = self.__ask_product_data()
      product.id = product_id
      self.__all_products.update(product)
    except ProductsDoNotExistException as e:
      print(str(e))
    except DistributorsDoNotExistException as e:
      print(str(e))

  def __ask_product_id(self):
    print("Produtos: ")
    products = self.__all_products.get_all()

    if len(products) == 0: raise ProductsDoNotExistException()

    for product in products:
      print(f"{product.id} - {product.name}")
    product_ids = tuple(map(lambda x: x.id, products))
    return helper.read_int("Qual você deseja atualizar? ", options=product_ids)


  def __ask_product_data(self):
    print("Atualizar produto")
    name = helper.read_string("Digite o nome: ", empty_valid=False)
    price = helper.read_float("Digite o preço: ", positive=True)
    distributor = self.__ask_for_distributor()
    return Product(None, name, price, distributor)

  def __ask_for_distributor(self):
    print("Selecione o distribuidor: ")
    distributors = self.__all_distributors.get_all()

    if len(distributors) == 0: raise DistributorsDoNotExistException()

    for distributor in distributors:
      print(f'{distributor.id} {distributor.name}')
    distributors_ids = tuple(map(lambda x: x.id, distributors))

    distributor_id = helper.read_int("Distribuidor: ", options=distributors_ids)
    return self.__all_distributors.get_by_id(distributor_id)