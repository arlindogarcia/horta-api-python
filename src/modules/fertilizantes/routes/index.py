
from src.modules.fertilizantes.controllers.FertilizanteController import FertilizanteController
from flask import request
from src.modules.fertilizantes.model.index import getModel

def getRoutes(app, db):
  fertilizantes = getModel(db)

  @app.route('/fertilizante', methods =['GET'])
  def listFertilizante():
    return FertilizanteController.list(fertilizantes, db)

  @app.route('/fertilizante/<id>', methods=["GET"])
  def showFertilizante(id):
    return FertilizanteController.show(fertilizantes, db, id)

  @app.route('/fertilizante', methods=["POST"])
  def createFertilizante():
    body = request.get_json()
    return FertilizanteController.create(fertilizantes, db, body)

  @app.route('/fertilizante/<id>', methods=["PUT"])
  def updateFertilizante(id):
    body = request.get_json()
    return FertilizanteController.update(fertilizantes, db, id, body)

  @app.route('/fertilizante/<id>', methods=["DELETE"])
  def deleteFertilizante(id):
    return FertilizanteController.delete(fertilizantes, db, id)