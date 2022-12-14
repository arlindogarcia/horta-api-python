from src.shared.methods.response import gera_response
from src.modules.categoria.model.index import getModel as modelCategoria
from src.modules.fertilizantes.model.index import getModel as modelFertilizante
from src.shared.methods.utils import converteDataToISO
def execute(hortalicas, db, id):
  categoria = modelCategoria(db)
  fertilizantes = modelFertilizante(db)

  objetos = hortalicas.query.filter_by(id=id).first()
  retorno = categoria.query.filter_by(id=objetos.categoria_id).first()
  objetos.categoria = retorno.to_json()
  retorno1 = fertilizantes.query.filter_by(id=objetos.fertilizantes_id).first()
  print(retorno1)
  retorno1.data_fabricacao = converteDataToISO(retorno1.data_fabricacao)
  retorno1.data_validade = converteDataToISO(retorno1.data_validade)
  print(retorno1)
  objetos.fertilizante = retorno1.to_json()
  resultado = objetos.to_json()
  return gera_response(200,'hortalica',resultado)