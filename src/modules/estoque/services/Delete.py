from src.shared.methods.response import gera_response

def execute(estoque, db, id):
  estoque_objetos = estoque.query.filter_by(id=id).first()
  try:
    db.session.delete(estoque_objetos)
    db.session.commit()
    return gera_response(200,'estoque', estoque_objetos.to_json(),'Deletado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "estoque",{},'Erro ao deletar' )