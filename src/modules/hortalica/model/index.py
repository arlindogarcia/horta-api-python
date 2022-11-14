from sqlalchemy import Column, Integer, String, Float, ForeignKey

def getModel(db):
  class hortalicas(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    nome = Column(String(100))
    largura = Column(Float)
    comprimento = Column(Float)
    altura = Column(Float)
    fertilizantes_id = Column(Integer, ForeignKey("fertilizantes.id"))
    fertilizante = ""
    categoria_id = Column(Integer, ForeignKey("categoria.id"))
    categoria = ""
    def to_json(self):
      return {"id": self.id,"nome": self.nome, "fertilizantes_id": self.fertilizantes_id, "categoria_id": self.categoria_id, "categoria": self.categoria, "fertilizante": self.fertilizante, "largura": self.largura, "comprimento": self.comprimento, "altura": self.altura}
  return hortalicas