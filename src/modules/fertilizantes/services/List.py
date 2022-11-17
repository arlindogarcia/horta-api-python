from src.shared.methods.response import gera_response
from src.modules.categoria.model.index import getModel as modelCategoria
from src.shared.methods.utils import converteDataToISO

def execute(fertilizantes, db):
  categoria = modelCategoria(db)

  objetos = fertilizantes.query.all()
  for item in objetos:
    retorno = categoria.query.filter_by(id=item.categoria_id).first()
    item.categoria = retorno.to_json()
    item.data_fabricacao = converteDataToISO(item.data_fabricacao)
    item.data_validade = converteDataToISO(item.data_validade)
  resultado = [itens.to_json() for itens in objetos]
  return gera_response(200,'fertilizante',resultado)