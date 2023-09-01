class IntegrityError(Exception):
  def __init__(self):
    super().__init__("Essa entidade não pode ser apagada por possuir dependencias.")