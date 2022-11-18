from sqlalchemy import Column, Integer, ForeignKey

def getModel(db):
  class horta_item(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    quantidade = Column(Integer)
    hortalicas_id = Column(Integer, ForeignKey("hortalicas.id"))
    hortalicas = ""
    horta_id = Column(Integer, ForeignKey("hortas.id"))
    horta = ""
    def to_json(self):
      return {"id": self.id, "hortalicas_id": self.hortalicas_id, "horta_id": self.horta_id, "horta": self.horta, "hortalicas": self.hortalicas, "quantidade": self.quantidade}
  return horta_item