
from src.modules.medicao.controllers.MedicaoController import MedicaoController
from flask import request
from src.modules.medicao.model.index import getModel

def getRoutes(app, db):
  medicao = getModel(db)

  @app.route('/medicao', methods =['GET'])
  def listMedicao():
    return MedicaoController.list(medicao, db)

  @app.route('/medicao/<id>', methods=["GET"])
  def showMedicao(id):
    return MedicaoController.show(medicao, db, id)

  @app.route('/medicao', methods=["POST"])
  def createMedicao():
    body = request.get_json()
    return MedicaoController.create(medicao, db, body)

  @app.route('/medicao/<id>', methods=["PUT"])
  def updateMedicao(id):
    body = request.get_json()
    return MedicaoController.update(medicao, db, id, body)

  @app.route('/medicao/<id>', methods=["DELETE"])
  def deleteMedicao(id):
    return MedicaoController.delete(medicao, db, id)