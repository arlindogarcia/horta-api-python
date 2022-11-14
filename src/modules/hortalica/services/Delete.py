from src.shared.methods.response import gera_response

def execute(hortalicas, db, id):
  hortalica = hortalicas.query.get(id)
  if not hortalica:
    return gera_response(200, "hortalica",{},'hortalica não existe!' )
  db.session.delete(hortalica)
  db.session.commit()
  return gera_response(200, "hortalica",{},'Deletado' )