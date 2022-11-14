
from src.modules.categoria.controllers.CategoriaController import CategoriaController
from flask import request
from src.modules.categoria.model.index import getModel

def getRoutes(app, db):
  categoria = getModel(db)

  @app.route('/categoria', methods =['GET'])
  def listCategoria():
    return CategoriaController.list(categoria, db)

  @app.route('/categoria/<id>', methods=["GET"])
  def showCategoria(id):
    return CategoriaController.show(categoria, db, id)

  @app.route('/categoria', methods=["POST"])
  def createCategoria():
    body = request.get_json()
    return CategoriaController.create(categoria, db, body)

  @app.route('/categoria/<id>', methods=["PUT"])
  def updateCategoria(id):
    body = request.get_json()
    return CategoriaController.update(categoria, db, id, body)

  @app.route('/categoria/<id>', methods=["DELETE"])
  def deleteCategoria(id):
    return CategoriaController.delete(categoria, db, id)