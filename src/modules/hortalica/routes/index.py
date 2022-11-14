
from src.modules.hortalica.controllers.HortalicaController import HortalicaController
from flask import request
from src.modules.hortalica.model.index import getModel

def getRoutes(app, db):
  hortalica = getModel(db)

  @app.route('/hortalica', methods =['GET'])
  def listHortalica():
    return HortalicaController.list(hortalica, db)

  @app.route('/hortalica/<id>', methods=["GET"])
  def showHortalica(id):
    return HortalicaController.show(hortalica, db, id)

  @app.route('/hortalica', methods=["POST"])
  def createHortalica():
    body = request.get_json()
    return HortalicaController.create(hortalica, db, body)

  @app.route('/hortalica/<id>', methods=["PUT"])
  def updateHortalica(id):
    body = request.get_json()
    return HortalicaController.update(hortalica, db, id, body)

  @app.route('/hortalica/<id>', methods=["DELETE"])
  def deleteHortalica(id):
    return HortalicaController.delete(hortalica, db, id)