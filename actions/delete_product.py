from repositories.products_repository import ProductsRepository
import helper


class DeleteProduct:
  @classmethod
  def build(cls):
    return cls(ProductsRepository.build())

  def __init__(self, all_products):
    self.__all_products = all_products

  def execute(self):
    print("Produtos: ")
    products = self.__all_products.get_all()
    for product in products:
      print(f"{product.id} - {product.name}")
    product_ids = tuple(map(lambda x: x.id, products))
    product_id = helper.read_int("Qual você deseja deletar? ", options=product_ids)
    product = self.__all_products.delete_by_id(product_id)