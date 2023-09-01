from exceptions.integrity_error import IntegrityError
from repositories.repository import Repository
from domain.address import Address
from domain.distributor import Distributor
from domain.product import Product


class ProductsRepository(Repository):
  def get_all(self):
    results = self._execute(self.__base_query())

    return tuple(map(self.__build_product, results))

  def get_by_id(self, id):
    results = self._execute(f"""
      {self.__base_query()}
        WHERE products.id = {id};
    """)
    return self.__build_product(results[0])

  def create(self, product):
    self._execute(f"""
      INSERT INTO products (name, price, distributor_id) VALUES
        ('{product.name}', {product.price}, {product.distributor_id});
    """)

  def delete_by_id(self, id):
    try:
      self._execute(f"""
        DELETE FROM products
          WHERE id = {id}
      """)
    except IntegrityError as e:
      print(str(e))

  def update(self, product):
    self._execute("""
      UPDATE products SET name = '{}', price = {}, distributor_id = {}
        WHERE id = {};
    """.format(product.name, product.price, product.distributor_id, product.id))

  def get_by_order_id(self, order_id):
    results = self._execute(f"""
      {self.__base_query()}
      JOIN order_product ON products.id = order_product.product_id
      WHERE order_product.order_id = {order_id};
    """)
    return tuple(map(self.__build_product, results))

  def delete_products_from_order_id(self, order_id):
    self._execute(f"""
      DELETE FROM order_product
        WHERE order_id = {order_id};
    """)

  def create_products_from_order(self, order):
    for product in order.products:
      self._execute(f"""
        INSERT INTO order_product (order_id, product_id)
          VALUES ({order.id}, {product.id});
      """)

  def __build_product(self, row):
    id = row[0]
    name = row[1]
    price = row[2]
    distributor = Distributor(row[3], row[4], Address(row[5], row[6], row[7], row[8]))
    return Product(id, name, price, distributor)

  def __base_query(self):
    return """
      SELECT
        products.id, products.name, products.price, distributors.id, distributors.name, street, city, state, number
        FROM products
        JOIN distributors ON distributors.id = distributor_id
        JOIN addresses On distributors.id = addresses.distributor_id
    """