from src.shared.methods.response import gera_response

def execute(estoque, db, body):
  try:
    cadastro_estoque = estoque(codigo= body["codigo"],origem_nome= body["origem_nome"],origem_id= body["origem_id"],quantidade= body["quantidade"],tipo_movimento= body["tipo_movimento"],cancelado= body["cancelado"],observacoes= body["observacoes"])
    db.session.add(cadastro_estoque)
    db.session.commit()
    return gera_response(200,'estoque', cadastro_estoque.to_json(),'Criado com Sucesso')
  except Exception as e:
    print(e)
    db.session.rollback()
    return gera_response(400, "estoque",{},'Erro ao cadastrar' )