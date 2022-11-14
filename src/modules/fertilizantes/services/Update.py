from src.shared.methods.response import gera_response

def execute(fertilizantes, db, id, body):
  objeto = fertilizantes.query.filter_by(id=id).first()
  try:
    objeto.nome = body['nome']
    objeto.fabricante = body["fabricante"]
    objeto.categoria_id = body["categoria_id"]
    db.session.add(objeto)
    db.session.commit()
    return gera_response(200,'fertilizante', objeto.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "fertilizante",{},'Erro ao cadastrar' )