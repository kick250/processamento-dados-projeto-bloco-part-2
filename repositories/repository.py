from sqlalchemy import create_engine, text, exc
from exceptions.integrity_error import IntegrityError


class Repository:
  @classmethod
  def build(cls):
    return cls()

  def __init__(self):
    string_connection = "mysql+mysqlconnector://root:@localhost/projeto_bloco"
    engine = create_engine(string_connection, echo=False)
    self.__engine = engine

  def _execute(self, query):
    try:
      results = None
      queries = query.strip().split(";")
      self.__remove_empty_queries(queries)
      with self.__engine.connect() as connection:
        res = None
        for query in queries:
          res = connection.execute(text(query))
        try:
          results = res.fetchall()
        except:
          results = res
        connection.commit()
      return results
    except exc.IntegrityError:
      raise IntegrityError()

  def __remove_empty_queries(self, queries):
    while("" in queries):
      queries.remove("")