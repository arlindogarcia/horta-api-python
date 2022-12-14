from src.config.database.db import getDB
from src.shared.http.app import getApp
from src.shared.http.routes.index import getRoutes

app = getApp()
db = getDB(app)

getRoutes(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    