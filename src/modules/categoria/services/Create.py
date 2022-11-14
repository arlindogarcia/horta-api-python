from src.shared.methods.response import gera_response

def execute(categoria, db, body):
  try:
    cadastro = categoria(nome= body["nome"])
    db.session.add(cadastro)
    db.session.commit()
    return gera_response(200,'categoria', cadastro.to_json(),'Criado com Sucesso')
  except Exception as e:
    db.session.rollback()
    return gera_response(400, "categoria",{},'Erro ao cadastrar')