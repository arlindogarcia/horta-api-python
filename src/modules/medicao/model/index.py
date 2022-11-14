from sqlalchemy import Column, Integer, ForeignKey, DateTime

def getModel(db):
  class medicao(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    valor_humidade = Column(Integer)
    data_leitura = Column(DateTime)
    horta_id = Column(Integer, ForeignKey("hortas.id"))
    horta = ""
    def to_json(self):
      return {"id": self.id,"valor_humidade": self.valor_humidade, "data_leitura": self.data_leitura, "horta_id": self.horta_id, "horta": self.horta}
  return medicao