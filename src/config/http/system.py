import socket

def getIpv4AddressLocal():
  return socket.gethostbyname(socket.gethostname())