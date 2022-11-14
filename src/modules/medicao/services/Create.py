from src.shared.methods.response import gera_response
from src.shared.methods.utils import converteDataToISO

def execute(medicao, db, body):
  try:
    cadastro = medicao(valor_humidade= body["valor_humidade"], data_leitura = body["data_leitura"], horta_id = body["horta_id"])
    db.session.add(cadastro)
    db.session.commit()
    cadastro.data_leitura = converteDataToISO(cadastro.data_leitura)
    return gera_response(201,'medicao', cadastro.to_json(),'Criado com Sucesso')
  except Exception as e:
    print(e)
    return gera_response(400, "medicao",{},'Erro ao cadastrar' )