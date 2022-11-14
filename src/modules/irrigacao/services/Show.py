from src.shared.methods.response import gera_response
from src.modules.horta.model.index import getModel as modelHorta
from src.shared.methods.utils import converteDataToISO

def execute(irrigacao, db, id):
  hortas = modelHorta(db)

  objetos = irrigacao.query.filter_by(id=id).first()
  objetos.data_irrigacao = converteDataToISO(objetos.data_irrigacao)
  retorno = hortas.query.filter_by(id=objetos.horta_id).first()
  objetos.horta = retorno.to_json()
  resultado = objetos.to_json()
  return gera_response(200,'irrigacao',resultado)