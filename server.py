import socket
import simplejson
from game import Tetroid
import copy, threading

class Server(threading.Thread):

  def __init__(self, host, port, game):

    threading.Thread.__init__(self)

    self.clients = []
    self.game = game
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((host, port))
    self.sock.listen(5)


  def run(self):
    running = 1
    while running:
      connection = self.sock.accept()
      self.accept(connection[0], connection[1])
      

  def accept(self, conn, addr):
    #Send out the info of the current board, the size etc.
    c = Client((conn,addr))
    c.start()
    self.clients.append(c)
    d = simplejson.JSONEncoder().encode([{"gridWidth":self.game.gridWidth},{"gridHeight":self.game.gridHeight},{"lines":self.game.lines}])
    conn.send(d)
    d = copy.copy(self.game.tetroids)
    d.append(self.game.currentTetroid)
    conn.send(simplejson.JSONEncoder(default=self.tetroidEncode).encode(d))
    print "Connection initated from ", addr


  def tetroidEncode(self,obj):
    if isinstance(obj, Tetroid):
      return {"type":obj.type, "colour":obj.colour, "squares":obj.squares}
    raise TypeError(repr(o) + " is not JSON serializable.")

class Client(threading.Thread):
  def __init__(self, (conn, addr)):
    threading.Thread.__init__(self)
    self.conn = conn
    self.addr = addr

  def send(self,data):
    self.conn.send(data)

