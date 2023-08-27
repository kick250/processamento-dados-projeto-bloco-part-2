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
    self._execute(f"""
      DELETE FROM products
        WHERE id = {id}
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