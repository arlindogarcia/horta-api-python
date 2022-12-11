from src.config.http.system import getIpv4AddressLocal

DB_USER = "root"
DB_PASS = "root"
DB_IP = getIpv4AddressLocal()
DB_PORT = "3306"
DB_DATABASE = "horta_banco"

def getConnection():
  return "mysql://" + DB_USER + ":" + DB_PASS + "@" + DB_IP + ":" + DB_PORT + "/" + DB_DATABASE