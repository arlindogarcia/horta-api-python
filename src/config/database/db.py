from  flask_sqlalchemy import SQLAlchemy

def getDB(app):
  db = SQLAlchemy(app)
  return db
