class DistributorNotFound(Exception):
  def __init__(self):
    super().__init__("Distribuir não encontrado")
