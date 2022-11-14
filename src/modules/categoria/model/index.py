from sqlalchemy import Column, Integer, String

def getModel(db):
  class categoria(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    nome = Column(String(100))

    def to_json(self):
      return {"id": self.id,"nome": self.nome}
  return categoria