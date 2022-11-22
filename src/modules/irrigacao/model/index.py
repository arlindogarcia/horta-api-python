from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float

def getModel(db):
  class irrigacao(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    data_irrigacao = Column(DateTime)
    horta_id = Column(Integer, ForeignKey("hortas.id"))
    valor_umidade = Column(Float)
    horta = ""
    def to_json(self):
      return {"id": self.id,"data_irrigacao": self.data_irrigacao, "horta_id": self.horta_id, "horta": self.horta, "valor_umidade": self.valor_umidade}
  return irrigacao