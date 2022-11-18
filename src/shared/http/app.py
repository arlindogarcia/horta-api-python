from flask import Flask
from src.config.database.connection import getConnection
from flask_cors import CORS

def getApp():
  app = Flask(__name__)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SQLALCHEMY_DATABASE_URI'] = getConnection()
  CORS(app)
  return app