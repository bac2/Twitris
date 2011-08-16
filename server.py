import socket

class Server:

  def __init__(self, host, port):

    self.clients = []
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((host, port))
    self.sock.listen(5)
    self.conn, self.addr = self.sock.accept()
    self.clients.append((self.conn,self.addr))
    
  def sendEvent(self, data):
    for x in self.clients:
      x[0].send(data)

