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
		self.lines = 0

	def left(self):
		tetroids = self.tetroids
		for x in self.currentTetroid.squares:
			for y in tetroids.squares:
				if(x[0]-1 == y[0] and x[1] == y[1]):
					#something to the left
					return

		for x in self.currentTetroid.squares:
			x[0] = x[0]-1

	def right(self):
		tetroids = self.tetroids
		for x in self.currentTetroid.squares:
			for y in tetroids.squares:
				if(x[0]+1 == y[0] and x[1] == y[1]):
					return
				#Something to the right

		for x in self.currentTetroid.squares:
			x[0] = x[0]+1

	def rotate(self):
		skip

	def occupied(self, x, y):
		for i in self.tetroids:
			for j in i.squares:
				if(j[0] == x and j[1] == y):
					return True
		return False

	def findMins(self):	
		mins = []
		for x in self.currentTetroid.squares:
			for y in self.currentTetroid.squares:
				curMin = y
				if(x[1] == y[1]): #y values are the same
					if(x[0]<y[0]):
						curMin = x
			if( curMin not in mins ):
				mins.append(curMin)
		return mins

	def clearBelow(self):
		
		for coord in mins:
			for x in self.tetroids:
				for y in x.squares:
					if( ( coord[0] == y[0] and coord[1]-1 == y[1] ) or coord[1] == 0 ):
						#Stop the shape
						return False
		return True

	def checkLines(self):
		for y in range(0, self.gridHeight):
			for x in range(0, self.gridWidth):
				if( not occupied(x,y)):
					continue
			print "line found!!"
			self.lines += 1
			#Move all lines above down by 1
			for i in self.tetroids:
				for q in i.squares:
					if(q[1] > y):
						q[1] -= 1

	def tick(self):
		#drop current tetroid 1 space
		mins = self.findMins()
		#mins holds minimum items, check below them.
		if(not clearBelow()):
			checkLines()
			self.currentTetroid = Tetroid()
			Tetroids.append(self.currentTetroid)
		
		else:
			#Nothing below then move down
			for x in self.currentTetroid.squares:
			x[1] = x[1]-1

