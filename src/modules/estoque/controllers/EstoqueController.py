from src.modules.estoque.services.List import execute as List
from src.modules.estoque.services.Show import execute as Show
from src.modules.estoque.services.Create import execute as Create
from src.modules.estoque.services.Update import execute as Update
from src.modules.estoque.services.Delete import execute as Delete

class EstoqueController():
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
  