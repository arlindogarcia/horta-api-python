from src.shared.methods.response import gera_response

def execute(categoria, db, id):
  objeto = categoria.query.filter_by(id=id).first()
  try:
    db.session.delete(objeto)
    db.session.commit()
    return gera_response(200,'categoria', objeto.to_json(),'Deletado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "categoria",{},'Erro ao deletar' )