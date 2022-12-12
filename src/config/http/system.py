import socket

def getIpv4AddressLocal():
  return socket.gethostbyname('Equipamento2') #Colocar o nome do computador que está rodando o container, para descobrir é só abrir o Terminal e rodar "HOSTNAME"