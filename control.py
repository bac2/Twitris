from game import *
from server import *
import random,copy

class Controller:

    def visualise(self):

        self.arr = []
        for x in range(0, 20):
            self.arr.append([])
            for y in range (0, 10):
                self.arr[x].append(0)

        for x in self.game.tetroids:
           for y in x.squares:
		print y[0], y[1]
                self.arr[y[1]][y[0]] = 1
	for y in self.game.currentTetroid.squares:
	    self.arr[y[1]][y[0]] = 1
	self.arr.reverse()
	for x in self.arr:
	    print x
	print 

    def sendEvent(self):
      data = copy.copy(self.game.tetroids)
      data.append(self.game.currentTetroid)
      d = simplejson.JSONEncoder(default=self.s.tetroidEncode).encode(data)
      for client in self.s.clients:
        client.send(d)

    def __init__(self):
      self.game = Game()
      self.visualise()
      self.s = Server("127.0.0.1", 6500, self.game)
      self.s.start()

      while 1:
        self.tick()
    
    def tick(self):
      self.visualise()
      self.game.tick()
      self.game.rotate()
      self.sendEvent()
      time.sleep(1)

c = Controller()
