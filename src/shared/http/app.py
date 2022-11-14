from flask import Flask
from src.config.database.connection import getConnection

def getApp():
  app = Flask(__name__)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SQLALCHEMY_DATABASE_URI'] = getConnection()
  return app