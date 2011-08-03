from game import *
import random
class Controller:

    def visualise(self):

        self.arr = []
        for x in range(0, 20):
            self.arr.append([])
            for y in range (0, 10):
                self.arr[x].append(0)

        for x in tetris.tetroids:
           for y in x.squares:
		print y[0], y[1]
                self.arr[y[1]][y[0]] = 1
	for y in tetris.currentTetroid.squares:
	    self.arr[y[1]][y[0]] = 1
	self.arr.reverse()
	for x in self.arr:
	    print x
	print 
c = Controller()
tetris = Game()
c.visualise()

while (True):
    c.visualise()
    tetris.tick()
    tetris.rotate()
    time.sleep(1)
