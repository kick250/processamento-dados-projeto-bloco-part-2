from repositories.orders_repository import OrdersRepository
import helper


class DeleteOrder:
  @classmethod
  def build(cls):
    return cls(OrdersRepository.build())

  def __init__(self, all_orders):
    self.__all_orders = all_orders

  def execute(self):
    orders = self.__all_orders.get_all()
    order_ids = []
    for order in orders:
      order_ids.append(order.id)
      print(f"{order.id} - {order.date}")

    order_id = helper.read_int("Qual você deseja deletar? ", options=order_ids)
    self.__all_orders.delete_by_id(order_id)