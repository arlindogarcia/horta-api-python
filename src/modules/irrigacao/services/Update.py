from src.shared.methods.response import gera_response
from src.shared.methods.utils import converteDataToISO

def execute(irrigacao, db, id, body):
  objeto = irrigacao.query.filter_by(id=id).first()
  try:
    objeto.data_irrigacao = body["data_irrigacao"]
    objeto.horta_id = body["horta_id"]
    objeto.valor_umidade = body["valor_umidade"]
    db.session.add(objeto)
    db.session.commit()
    objeto.data_irrigacao = converteDataToISO(objeto.data_irrigacao)
    return gera_response(200,'irrigacao', objeto.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "irrigacao",{},'Erro ao cadastrar' )