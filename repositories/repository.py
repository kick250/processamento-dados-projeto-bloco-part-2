from sqlalchemy import create_engine, text


class Repository:
  @classmethod
  def build(cls):
    return cls()

  def __init__(self):
    string_connection = "mysql+mysqlconnector://root:@localhost/projeto_bloco"
    engine = create_engine(string_connection, echo=False)
    self.__engine = engine

  def _execute(self, query):
    results = None
    with self.__engine.connect() as connection:
      res = connection.execute(text(query))
      try:
        results = res.fetchall()
      except:
        results = res
      connection.commit()
    return results