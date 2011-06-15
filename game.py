import random, time

class Tetroid:
	def __init__(self):
		self.type = random.randint(0,4)
		self.colour = random.randint(0,4)
		self.squares = [(8,8), (8,9), (9,9), (9,8)]
class Game:
	def __init__(self):
		self.tetroids = []
		self.gridHeight = 20
		self.gridWidth = 10
		self.currentTetroid = Tetroid()
		self.tetroids.append(self.currentTetroid)
		self.run()

	def left():
		skip
	def right():
		skip
	def rotate():
		skip

        def tick(self):
		#drop current tetroid 1 space
		i = 0
		for x in self.currentTetroid.squares:
			while(i < len(self.currentTetroid.squares)-1):
				print x[1]
				i += 1

        def run(self):
		while True:
			self.tick()
			
			

