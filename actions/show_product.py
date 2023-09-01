from repositories.products_repository import ProductsRepository
import helper


class ShowProduct:
  @classmethod
  def build(cls):
    return cls(ProductsRepository.build())

  def __init__(self, all_products):
    self.__all_products = all_products

  def execute(self):
    print("Produtos: ")
    products = self.__all_products.get_all()

    if len(products) == 0: return print("Não existem produtos.")

    for product in products:
      print(f"{product.id} - {product.name}")
    product_ids = tuple(map(lambda x: x.id, products))
    product_id = helper.read_int("Qual você deseja ver? ", options=product_ids)
    product = self.__all_products.get_by_id(product_id)

    print()
    print("---------------------------")
    print(f"Id: {product.id}")
    print(f"Nome: {product.name}")
    print(f"Preço: {product.price}")
    print(f"Distribuidor: {product.distributor_name}")
    print("---------------------------")
