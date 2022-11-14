from src.shared.methods.response import gera_response

def execute(irrigacao, db, id):
  retorno = irrigacao.query.get(id)
  if not retorno:
    return gera_response(200, "irrigacao",{},'irrigacao não existe!' )
  db.session.delete(retorno)
  db.session.commit()
  return gera_response(200, "irrigacao",{},'Deletado' )