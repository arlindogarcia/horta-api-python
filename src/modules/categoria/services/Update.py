from src.shared.methods.response import gera_response

def execute(categoria, db, id, body):
  objetos = categoria.query.filter_by(id=id).first()
  try:
    objetos.nome = body['nome']
    db.session.add(objetos)
    db.session.commit()
    return gera_response(200,'categoria', objetos.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "categoria",{},'Erro ao cadastrar' )