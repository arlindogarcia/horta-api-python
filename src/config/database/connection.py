DB_USER = "root"
DB_PASS = "1012"
DB_IP = "localhost"
DB_PORT = "3336"
DB_DATABASE = "horta_banco"

def getConnection():
  return "mysql://" + DB_USER + ":" + DB_PASS + "@" + DB_IP + ":" + DB_PORT + "/" + DB_DATABASE