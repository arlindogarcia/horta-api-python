from src.shared.methods.response import gera_response

def execute(estoque, db):
  estoque_objetos = estoque.query.all()
  estoque_json = [itens.to_json() for itens in estoque_objetos]
  return gera_response(200,'estoque',estoque_json)