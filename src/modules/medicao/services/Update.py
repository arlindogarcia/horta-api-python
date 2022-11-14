from src.shared.methods.response import gera_response
from src.shared.methods.utils import converteDataToISO

def execute(medicao, db, id, body):
  objeto = medicao.query.filter_by(id=id).first()
  try:
    objeto.valor_humidade = body['valor_humidade']
    objeto.data_leitura = body["data_leitura"]
    objeto.horta_id = body["horta_id"]
    db.session.add(objeto)
    db.session.commit()
    objeto.data_leitura = converteDataToISO(objeto.data_leitura)
    return gera_response(200,'medicao', objeto.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "medicao",{},'Erro ao cadastrar' )