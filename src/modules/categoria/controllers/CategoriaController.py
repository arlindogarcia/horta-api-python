from src.modules.categoria.services.List import execute as List
from src.modules.categoria.services.Show import execute as Show
from src.modules.categoria.services.Create import execute as Create
from src.modules.categoria.services.Update import execute as Update
from src.modules.categoria.services.Delete import execute as Delete

class CategoriaController():
  def list(categoria, db):
    return List(categoria, db)
  
  def show(categoria, db, id):
    return Show(categoria, db, id)
  
  def create(categoria, db, body):
    return Create(categoria, db, body)

  def update(categoria, db, id, body):
    return Update(categoria, db, id, body)
  
  def delete(categoria, db, id):
    return Delete(categoria, db, id)
  