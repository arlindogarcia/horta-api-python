
from src.modules.irrigacao.controllers.IrricacaoController import IrricacaoController
from flask import request
from src.modules.irrigacao.model.index import getModel

def getRoutes(app, db):
  irrigacao = getModel(db)

  @app.route('/irrigacao', methods =['GET'])
  def listIrrigacao():
    return IrricacaoController.list(irrigacao, db)

  @app.route('/irrigacao/<id>', methods=["GET"])
  def showIrrigacao(id):
    return IrricacaoController.show(irrigacao, db, id)

  @app.route('/irrigacao', methods=["POST"])
  def createIrrigacao():
    body = request.get_json()
    return IrricacaoController.create(irrigacao, db, body)

  @app.route('/irrigacao/<id>', methods=["PUT"])
  def updateIrrigacao(id):
    body = request.get_json()
    return IrricacaoController.update(irrigacao, db, id, body)

  @app.route('/irrigacao/<id>', methods=["DELETE"])
  def deleteIrrigacao(id):
    return IrricacaoController.delete(irrigacao, db, id)