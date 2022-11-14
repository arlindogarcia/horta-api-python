from src.shared.methods.response import gera_response
from src.modules.horta.model.index import getModel as modelHorta
from src.shared.methods.utils import converteDataToISO

def execute(medicao, db):
  hortas = modelHorta(db)

  objetos = medicao.query.all()
  for item in objetos:
    retorno = hortas.query.filter_by(id=item.horta_id).first()
    item.horta = retorno.to_json()
    item.data_leitura = converteDataToISO(item.data_leitura)

  resultado = [itens.to_json() for itens in objetos]
  print(resultado)
  return gera_response(200,'medicao',resultado)