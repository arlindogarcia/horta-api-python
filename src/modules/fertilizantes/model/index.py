from sqlalchemy import Column, Integer, String, ForeignKey, Date

def getModel(db):
  class fertilizantes(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    nome = Column(String(100))
    fabricante = Column(String(100))
    data_fabricacao = Column(Date)
    data_validade = Column(Date)
    categoria_id = Column(Integer, ForeignKey("categoria.id"))
    categoria = ""
    def to_json(self):
      return {"id": self.id,"nome": self.nome, "fabricante": self.fabricante,'data_fabricacao': self.data_fabricacao,'data_validade': self.data_validade, "categoria_id": self.categoria_id, "categoria": self.categoria}
  return fertilizantes