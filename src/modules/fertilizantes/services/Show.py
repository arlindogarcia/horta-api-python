from src.shared.methods.response import gera_response
from src.modules.categoria.model.index import getModel as modelCategoria
from src.shared.methods.utils import converteDataToISO

def execute(fertilizantes, db, id):
  categoria = modelCategoria(db)
  obj = fertilizantes.query.filter_by(id=id).first()
  obj.data_fabricacao = converteDataToISO(obj.data_fabricacao)
  obj.data_validade = converteDataToISO(obj.data_validade)
  retorno = categoria.query.filter_by(id=obj.categoria_id).first()
  obj.categoria = retorno.to_json()
  resultado = obj.to_json()
  return gera_response(200,'fertilizante', resultado)