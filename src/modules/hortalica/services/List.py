from src.shared.methods.response import gera_response
from src.modules.categoria.model.index import getModel as modelCategoria
from src.modules.fertilizantes.model.index import getModel as modelFertilizante

def execute(hortalicas, db):
  categoria = modelCategoria(db)
  fertilizantes = modelFertilizante(db)

  objetos = hortalicas.query.all()
  for item in objetos:
    retorno = categoria.query.filter_by(id=item.categoria_id).first()
    retorno1 = fertilizantes.query.filter_by(id=item.fertilizantes_id).first()
    item.categoria = retorno.to_json()
    item.fertilizante = retorno1.to_json()
  resultado = [itens.to_json() for itens in objetos]

  return gera_response(200,'hortalica',resultado)