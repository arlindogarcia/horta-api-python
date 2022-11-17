from flask import Response
import json

def gera_response(status, nome_conteudo, conteudo, mensagem = False):
  body = {}
  if(mensagem):
    body['mensagem'] = mensagem
  return Response(json.dumps(conteudo),status=status,mimetype='application/json')