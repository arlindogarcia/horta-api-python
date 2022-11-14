
from src.modules.horta.controllers.HortaController import HortaController
from flask import request
from src.modules.horta.model.index import getModel

def getRoutes(app, db):
  horta = getModel(db)

  @app.route('/horta', methods =['GET'])
  def listHorta():
    return HortaController.list(horta, db)

  @app.route('/horta/<id>', methods=["GET"])
  def showHorta(id):
    return HortaController.show(horta, db, id)

  @app.route('/horta', methods=["POST"])
  def createHorta():
    body = request.get_json()
    return HortaController.create(horta, db, body)

  @app.route('/horta/<id>', methods=["PUT"])
  def updateHorta(id):
    body = request.get_json()
    return HortaController.update(horta, db, id, body)

  @app.route('/horta/<id>', methods=["DELETE"])
  def deleteHorta(id):
    return HortaController.delete(horta, db, id)