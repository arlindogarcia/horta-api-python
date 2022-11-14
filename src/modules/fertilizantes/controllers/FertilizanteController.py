from src.modules.fertilizantes.services.List import execute as List
from src.modules.fertilizantes.services.Show import execute as Show
from src.modules.fertilizantes.services.Create import execute as Create
from src.modules.fertilizantes.services.Update import execute as Update
from src.modules.fertilizantes.services.Delete import execute as Delete

class FertilizanteController():
  def list(fertilizante, db):
    return List(fertilizante, db)
  
  def show(fertilizante, db, id):
    return Show(fertilizante, db, id)
  
  def create(fertilizante, db, body):
    return Create(fertilizante, db, body)

  def update(fertilizante, db, id, body):
    return Update(fertilizante, db, id, body)
  
  def delete(fertilizante, db, id):
    return Delete(fertilizante, db, id)
  