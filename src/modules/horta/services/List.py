from src.shared.methods.response import gera_response
from src.modules.horta_item.model.index import getModel as modelHortaItem
from src.modules.hortalica.model.index import getModel as modelHortalica

def execute(hortas, db):
  horta_item = modelHortaItem(db)
  hortalicas = modelHortalica(db)

  objetos = hortas.query.all()
  for item in objetos:
    retorno = horta_item.query.filter_by(horta_id=item.id).all()

    for i in retorno:
      hortalicas_retorno = hortalicas.query.filter_by(id=i.hortalicas_id).first()
      i.hortalicas = hortalicas_retorno.to_json()

    item.horta_items = [itens.to_json() for itens in retorno]
  resultado = [itens.to_json() for itens in objetos]

  return gera_response(200,'horta',resultado)