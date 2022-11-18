from src.shared.methods.response import gera_response
from src.shared.methods.utils import converteDataToISO

def execute(fertilizantes, db, body):
  try:
    cadastro = fertilizantes(nome= body["nome"], fabricante = body["fabricante"], categoria_id = body["categoria_id"],data_fabricacao= body['data_fabricacao'],data_validade= body['data_validade'])
    db.session.add(cadastro)
    db.session.commit()
    cadastro.data_fabricacao = converteDataToISO(cadastro.data_fabricacao)
    cadastro.data_validade = converteDataToISO(cadastro.data_validade)
    return gera_response(201,'fertilizante', cadastro.to_json(),'Criado com Sucesso')
  except Exception as e:
    print(e)
    return gera_response(400, "fertilizante",{},'Erro ao cadastrar' )