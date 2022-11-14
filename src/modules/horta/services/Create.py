from src.shared.methods.response import gera_response
from src.modules.horta_item.model.index import getModel as modelHortaItem

def execute(hortas, db, body):
  horta_item = modelHortaItem(db)

  try:
    cadastro = hortas(nome_horta= body["nome_horta"], area_plantio = body["area_plantio"])
    db.session.add(cadastro)
    db.session.commit()

    for i in body["horta_items"]:
      hortai_cadastro = horta_item(quantidade= i["quantidade"], hortalicas_id = i["hortalicas_id"], horta_id = cadastro.id)
      db.session.add(hortai_cadastro)
      db.session.commit()
    return gera_response(201,'horta', cadastro.to_json(),'Criado com Sucesso')
  except Exception as e:
    print(e)
    return gera_response(400, "horta",{},'Erro ao cadastrar' )