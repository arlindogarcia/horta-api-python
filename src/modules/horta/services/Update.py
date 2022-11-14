from src.shared.methods.response import gera_response
from src.modules.horta_item.model.index import getModel as modelHortaItem

def execute(hortas, db, id, body):
  horta_item = modelHortaItem(db)
  objeto = hortas.query.filter_by(id=id).first()
  try:
    objeto.nome_horta = body['nome_horta']
    objeto.area_plantio = body["area_plantio"]
    db.session.add(objeto)
    db.session.commit()

    objeto_items = horta_item.query.filter_by(horta_id=objeto.id).all()
    for obj in objeto_items:
      retorno = horta_item.query.get(obj.id)
      db.session.delete(retorno)
      db.session.commit()
    
    for i in body["horta_items"]:
      hortai_cadastro = horta_item(quantidade= i["quantidade"], hortalicas_id = i["hortalicas_id"], horta_id = objeto.id)
      db.session.add(hortai_cadastro)
      db.session.commit()
    return gera_response(200,'horta', objeto.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "horta",{},'Erro ao cadastrar' )