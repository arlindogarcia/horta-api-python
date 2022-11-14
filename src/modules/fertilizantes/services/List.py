from src.shared.methods.response import gera_response
from src.modules.categoria.model.index import getModel as modelCategoria

def execute(fertilizantes, db):
  categoria = modelCategoria(db)

  objetos = fertilizantes.query.all()
  for item in objetos:
    retorno = categoria.query.filter_by(id=item.categoria_id).first()
    item.categoria = retorno.to_json()
  resultado = [itens.to_json() for itens in objetos]
  print(resultado)
  return gera_response(200,'fertilizante',resultado)