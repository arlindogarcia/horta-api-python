from src.modules.medicao.services.List import execute as List
from src.modules.medicao.services.Show import execute as Show
from src.modules.medicao.services.Create import execute as Create
from src.modules.medicao.services.Update import execute as Update
from src.modules.medicao.services.Delete import execute as Delete

class MedicaoController():
  def list(item, db):
    return List(item, db)
  
  def show(item, db, id):
    return Show(item, db, id)
  
  def create(item, db, body):
    return Create(item, db, body)

  def update(item, db, id, body):
    return Update(item, db, id, body)
  
  def delete(item, db, id):
    return Delete(item, db, id)
  