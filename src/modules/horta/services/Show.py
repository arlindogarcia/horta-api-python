from src.shared.methods.response import gera_response
from src.modules.horta_item.model.index import getModel as modelHortaItem
from src.modules.hortalica.model.index import getModel as modelHortalica

def execute(hortas, db, id):
  horta_item = modelHortaItem(db)
  hortalicas = modelHortalica(db)

  objetos = hortas.query.filter_by(id=id).first()
  retorno = horta_item.query.filter_by(horta_id=objetos.id).all()
  for i in retorno:
      hortalicas_retorno = hortalicas.query.filter_by(id=i.hortalicas_id).first()
      i.hortalicas = hortalicas_retorno.to_json()
  objetos.horta_items = [itens.to_json() for itens in retorno]
  resultado = objetos.to_json()
  return gera_response(200,'horta',resultado)