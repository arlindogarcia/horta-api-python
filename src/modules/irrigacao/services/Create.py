from src.shared.methods.response import gera_response
from src.shared.methods.utils import converteDataToISO

def execute(irrigacao, db, body):
  try:
    cadastro = irrigacao(data_irrigacao = body["data_irrigacao"], horta_id = body["horta_id"])
    db.session.add(cadastro)
    db.session.commit()
    cadastro.data_irrigacao = converteDataToISO(cadastro.data_irrigacao)
    return gera_response(201,'irrigacao', cadastro.to_json(),'Criado com Sucesso')
  except Exception as e:
    print(e)
    return gera_response(400, "irrigacao",{},'Erro ao cadastrar' )