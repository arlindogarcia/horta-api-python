from src.shared.methods.response import gera_response

def execute(fertilizantes, db, id):
  fertilizante = fertilizantes.query.get(id)
  if not fertilizante:
    return gera_response(200, "fertilizante",{},'Fertilizante não existe!' )
  db.session.delete(fertilizante)
  db.session.commit()
  return gera_response(200, "fertilizante",{},'Deletado' )