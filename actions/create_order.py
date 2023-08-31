from repositories.orders_repository import OrdersRepository
from repositories.products_repository import ProductsRepository
from domain.order import Order
import helper


class CreateOrder:
  @classmethod
  def build(cls):
    return cls(OrdersRepository.build(), ProductsRepository.build())

  def __init__(self, all_orders, all_products):
    self.__all_orders = all_orders
    self.__all_products = all_products

  def execute(self):
    date = helper.read_date("Qual a data do pedido(dd/mm/yyyy)? ")
    products = self.read_products()
    order = Order(None, date, products)
    self.__all_orders.create(order)

  def read_products(self):
    selected_products = []

    products = self.__all_products.get_all()
    product_ids = tuple(map(lambda x: x.id, products))
    while True:
      for product in products:
        print(f"{product.id} - {product.name}")
      product_id = helper.read_int("Qual você deseja adicionar? ", options=product_ids)
      selected_products.append(self.__all_products.get_by_id(product_id))
      if not helper.confirm("Deseja adicionar mais produtos(S/N)? "): break
    return selected_products
