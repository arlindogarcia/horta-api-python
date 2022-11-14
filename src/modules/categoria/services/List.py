from src.shared.methods.response import gera_response

def execute(categoria, db):
  objetos = categoria.query.all()
  json = [itens.to_json() for itens in objetos]
  return gera_response(200,'categoria',json)