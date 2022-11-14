from sqlalchemy import Column, Integer, String, Float

def getModel(db):
  class hortas(db.Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    nome_horta = Column(String(100))
    area_plantio = Column(Float)
    horta_items = []
    def to_json(self):
      return {"id": self.id,"nome_horta": self.nome_horta, "area_plantio": self.area_plantio, "horta_items": self.horta_items}
  return hortas