from src.modules.categoria.routes.index import getRoutes as categoria
from src.modules.fertilizantes.routes.index import getRoutes as fertilizante
from src.modules.estoque.routes.index import getRoutes as estoque
from src.modules.hortalica.routes.index import getRoutes as hortalica
from src.modules.horta.routes.index import getRoutes as horta
from src.modules.irrigacao.routes.index import getRoutes as irrigacao
from src.modules.medicao.routes.index import getRoutes as medicao

def getRoutes(app, db):
  {
    'categoria': categoria(app, db),
    'fertilizante': fertilizante(app, db),
    'estoque': estoque(app, db),
    'hortalica': hortalica(app, db),
    'horta': horta(app, db),
    'irrigacao': irrigacao(app, db),
    'medicao': medicao(app, db),
  }