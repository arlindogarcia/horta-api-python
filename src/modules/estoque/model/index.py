from sqlalchemy import Column, Integer, String, Float, Text

def getModel(db):
  class estoque(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    codigo = Column(String(100))
    origem_nome = Column(String(100))
    origem_id = Column(String(100))
    quantidade = Column(Float)
    tipo_movimento = Column(Integer)
    cancelado = Column(Integer)
    observacoes = Column(Text)
    def to_json(self):
      return {"id": self.id,"codigo": self.codigo,"origem_nome": self.origem_nome, "origem_id": self.origem_id, "quantidade": self.quantidade, "tipo_movimento": self.tipo_movimento,'cancelado': self.cancelado,'observacoes': self.observacoes}
  return estoque