from src.shared.methods.response import gera_response

def execute(hortalicas, db, id, body):
  objeto = hortalicas.query.filter_by(id=id).first()
  try:
    objeto.nome = body['nome']
    objeto.largura = body["largura"]
    objeto.comprimento = body["comprimento"]
    objeto.altura = body["altura"]
    objeto.fertilizantes_id = body["fertilizantes_id"]
    objeto.categoria_id = body["categoria_id"]
    db.session.add(objeto)
    db.session.commit()
    return gera_response(200,'hortalica', objeto.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "hortalica",{},'Erro ao cadastrar' )