from src.shared.methods.response import gera_response

def execute(categoria, db, id):
  objeto = categoria.query.filter_by(id=id).first()
  json = objeto.to_json()
  return gera_response(200,'categoria',json)