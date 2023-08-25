from sqlalchemy import create_engine, text


class Repository:
  @classmethod
  def build(cls):
    string_connection = "mysql+mysqlconnector://root:123456@localhost/projeto_bloco"
    engine = create_engine(string_connection, echo=False)
    return cls(engine)

  def __init__(self, engine):
    self.__engine = engine

  def _execute(self, query):
    results = None
    with self.__engine.connect() as connection:
      res = connection.execute(text(query))
      try:
        results = res.fetchall()
      except:
        pass
      connection.commit()
    return results