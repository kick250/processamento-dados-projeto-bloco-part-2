class OrdersDoNotExistException(Exception):
  def __init__(self):
    super().__init__("Impossivel realizar esta ação sem pedidos criados.")