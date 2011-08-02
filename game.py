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
		for x in self.findLefts():
			if( x[0] <= 0):
				return False
			for y in self.tetroids:
			    for z in y.squares:
				if(x[0]-1 == z[0] and x[1] == z[1]):
					#something to the left
					return False

		for x in self.currentTetroid.squares:
			x[0] = x[0]-1

	def right(self):
		
		for x in self.findRights():
			if( x[0] >= self.gridWidth-1):
				return False
			for y in self.tetroids:
                            for z in y.squares:
				if(x[0]+1 == z[0] and x[1] == z[1]):
					return False
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

	def findLefts(self):	
		self.lefts = []
		for square in self.currentTetroid.squares:
		    if(len(self.lefts) == 0):
		        self.lefts.append(square)
		    else:
                        for x in self.lefts:
			    if(square[1] == x[1] and square[0] < x[0]):
			        self.lefts.append(square)
			        self.lefts.remove(x)
		return self.lefts

	def findRights(self):	
		self.rights = []
		for square in self.currentTetroid.squares:
		    if(len(self.rights) == 0):
		        self.rights.append(square)
		    else:
                        for x in self.rights:
			    if(square[1] == x[1] and square[0] > x[0]):
			        self.rights.append(square)
			        self.rights.remove(x)
		return self.rights

	def findMins(self):	
		self.mins = []
		for square in self.currentTetroid.squares:
		    if( len(self.mins) == 0):
		        self.mins.append(square)
		    else:
		        for x in self.mins:
			    if(square[0] == x[0] and square[0] < x[0]):
			        self.mins.append(square)
			        self.mins.remove(x)
		return self.mins

	def clearBelow(self):
		self.mins = self.findMins()	
		for coord in self.mins:
			for x in self.tetroids:
				for y in x.squares:
					if( ( coord[0] == y[0] and coord[1]-1 == y[1] ) or coord[1] == 0 ):
						#Stop the shape
						return False
		return True

	def checkLines(self):
		for y in range(0, self.gridHeight):
			for x in range(0, self.gridWidth):
				if( not self.occupied(x,y)):
					self.line = False
			if( not self.line ):
			    continue;
			print "line found!!"
			self.lines += 1
			#Move all lines above down by 1
			for i in self.tetroids:
				for q in i.squares:
					if(q[1] > y):
						q[1] -= 1

	def tick(self):
		#drop current tetroid 1 space
		self.mins = self.findMins()
		#mins holds minimum items, check below them.
		
		if( not self.clearBelow() ):
			self.checkLines()
			self.currentTetroid = Tetroid()
			self.tetroids.append(self.currentTetroid)
		
		else:
			#Nothing below then move down
			for x in self.currentTetroid.squares:
				x[1] = x[1]-1

