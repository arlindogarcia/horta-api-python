from src.shared.methods.response import gera_response

def execute(hortalicas, db, body):
  try:
    cadastro = hortalicas(nome= body["nome"], largura = body["largura"], comprimento = body["comprimento"], altura = body["altura"], categoria_id = body["categoria_id"], fertilizantes_id = body["fertilizantes_id"])
    db.session.add(cadastro)
    db.session.commit()
    return gera_response(201,'hortalica', cadastro.to_json(),'Criado com Sucesso')
  except Exception as e:
    print(e)
    return gera_response(400, "hortalica",{},'Erro ao cadastrar' )