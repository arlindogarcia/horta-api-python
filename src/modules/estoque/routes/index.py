
from src.modules.estoque.controllers.EstoqueController import EstoqueController
from flask import request
from src.modules.estoque.model.index import getModel

def getRoutes(app, db):
  estoque = getModel(db)

  @app.route('/estoque', methods =['GET'])
  def listEstoque():
    return EstoqueController.list(estoque, db)

  @app.route('/estoque/<id>', methods=["GET"])
  def showEstoque(id):
    return EstoqueController.show(estoque, db, id)

  @app.route('/estoque', methods=["POST"])
  def createEstoque():
    body = request.get_json()
    return EstoqueController.create(estoque, db, body)

  @app.route('/estoque/<id>', methods=["PUT"])
  def updateEstoque(id):
    body = request.get_json()
    return EstoqueController.update(estoque, db, id, body)

  @app.route('/estoque/<id>', methods=["DELETE"])
  def deleteEstoque(id):
    return EstoqueController.delete(estoque, db, id)