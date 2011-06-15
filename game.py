import random, time

class Tetroid:
	def __init__(self):
		self.type = random.randint(0,4)
		self.colour = random.randint(0,4)
		self.squares = [[8,8], [8,9], [9,9], [9,8]]
class Game:
	def __init__(self):
		self.tetroids = []
		self.gridHeight = 20
		self.gridWidth = 10
		self.currentTetroid = Tetroid()
		self.tetroids.append(self.currentTetroid)

	def left():
		skip
	def right():
		skip
	def rotate():
		skip

        def tick(self):
		#drop current tetroid 1 space
		mins = []
		for x in self.currentTetroid.squares:
			for y in self.currentTetroid.squares:
				curMin = y
				if(x[1] == y[1]): #y values are the same
					if(x[0]<y[0]):
						curMin = x
			if( curMin not in mins ):
				mins.append(curMin)
		print mins
		#mins holds minimum items, check below them.
		for coord in mins:
			for x in self.tetroids:
				for y in x.squares:
					if(coord[0] == y[0] and coord[1]-1 == y[1] ):
						
						print coord[0]-1, y[0]

		#Nothing below then move down

		for x in self.currentTetroid.squares:
			x[1] = x[1]-1

		print self.currentTetroid.squares

        def run(self):
		self.tick()
