from src.shared.methods.response import gera_response

def execute(estoque, db, id):
  estoque_objetos = estoque.query.filter_by(id=id).first()
  estoque_json = estoque_objetos.to_json()
  return gera_response(200,'estoque',estoque_json)