from src.shared.methods.response import gera_response

def execute(medicao, db, id):
  retorno = medicao.query.get(id)
  if not retorno:
    return gera_response(200, "medicao",{},'medicao não existe!' )
  db.session.delete(retorno)
  db.session.commit()
  return gera_response(200, "medicao",{},'Deletado' )