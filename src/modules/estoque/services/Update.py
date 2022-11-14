from src.shared.methods.response import gera_response

def execute(estoque, db, id, body):
  objeto = estoque.query.filter_by(id=id).first()
  try:
    objeto.codigo = body['codigo']
    objeto.origem_nome = body["origem_nome"]
    objeto.origem_id = body["origem_id"]
    objeto.quantidade = body["quantidade"]
    objeto.tipo_movimento = body["tipo_movimento"]
    objeto.cancelado = body["cancelado"]
    objeto.observacoes = body["observacoes"]
    db.session.add(objeto)
    db.session.commit()
    return gera_response(200,'estoque', objeto.to_json(),'Alterado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "estoque",{},'Erro ao cadastrar' )