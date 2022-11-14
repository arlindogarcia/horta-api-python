from src.shared.methods.response import gera_response
from src.modules.horta_item.model.index import getModel as modelHortaItem

def execute(hortas, db, id):
  horta_item = modelHortaItem(db)
  retorno = hortas.query.get(id)
  if not retorno:
    return gera_response(200, "horta",{},'horta não existe!' )

  objeto_items = horta_item.query.filter_by(horta_id=retorno.id).all()
  for obj in objeto_items:
    retorno_item = horta_item.query.get(obj.id)
    db.session.delete(retorno_item)
    db.session.commit()

  db.session.delete(retorno)
  db.session.commit()
  return gera_response(200, "horta",{},'Deletado' )