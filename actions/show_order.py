from repositories.orders_repository import OrdersRepository
import helper


class ShowOrder:
  @classmethod
  def build(cls):
    return cls(OrdersRepository.build())

  def __init__(self, all_orders):
    self.__all_orders = all_orders

  def execute(self):
    orders = self.__all_orders.get_all()

    if len(orders) == 0: return print("Não existem pedidos.")

    order_ids = []
    for order in orders:
      order_ids.append(order.id)
      print(f"{order.id} - {order.formatted_date}")

    order_id = helper.read_int("Qual você deseja ver? ", options=order_ids)

    order = self.__all_orders.get_by_id(order_id)
    print("-------------------------")
    print(f"Id: {order.id}")
    print(f"Data: {order.formatted_date}")
    print("produtos: ")
    for product in order.products:
      print(f"- {product.name}({product.distributor_name})")
    print("-------------------------")
