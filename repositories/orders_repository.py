from domain.order import Order
from repositories.repository import Repository
from repositories.products_repository import ProductsRepository


class OrdersRepository(Repository):
  @classmethod
  def build(cls):
    return cls(ProductsRepository.build())

  def __init__(self, all_products):
    self.__all_products = all_products
    super().__init__()

  def get_all(self):
    results = self._execute("""SELECT id, date FROM orders;""")
    return tuple(map(self.__build_order, results))

  def get_by_id(self, id):
    results = self._execute(f"""
      SELECT id, date FROM orders
        WHERE id = {id};
    """)
    return self.__build_order(results[0])

  def create(self, order):
    result = self._execute(f"INSERT INTO orders (date) VALUES ('{str(order.date)}');")
    order.id = result.lastrowid

    self.__all_products.delete_products_from_order_id(order.id)
    self.__all_products.create_products_from_order(order)

  def delete_by_id(self, order_id):
    self.__all_products.delete_products_from_order_id(order_id)
    self._execute(f"DELETE FROM orders WHERE id = {order_id};")

  def __build_order(self, row):
    id = row[0]
    date = row[1]
    products = self.__all_products.get_by_order_id(id)
    return Order(id, date, products)