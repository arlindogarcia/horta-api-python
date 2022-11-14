from sqlalchemy import Column, Integer, String, ForeignKey

def getModel(db):
  class fertilizantes(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    nome = Column(String(100))
    fabricante = Column(String(100))
    categoria_id = Column(Integer, ForeignKey("categoria.id"))
    categoria = ""
    def to_json(self):
      return {"id": self.id,"nome": self.nome, "fabricante": self.fabricante, "categoria_id": self.categoria_id, "categoria": self.categoria}
  return fertilizantes