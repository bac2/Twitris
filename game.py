import random, time

class Tetroid:
	def __init__(self, tetris):
		self.type = random.randint(0,6)
		self.colour = random.randint(0,4)
		self.mid = tetris.gridWidth / 2
		self.gridHeight = tetris.gridHeight-1
		if(self.type == 0): #Long shape
		    self.squares = [[self.mid,self.gridHeight],
				    [self.mid,self.gridHeight-1],
				    [self.mid,self.gridHeight-2],
				    [self.mid,self.gridHeight-3]]
		elif(self.type == 1): #S shape
		    self.squares = [[self.mid,self.gridHeight],
				    [self.mid+1, self.gridHeight],
				    [self.mid,self.gridHeight-1],
				    [self.mid-1,self.gridHeight-1]]
		elif(self.type == 2): #T Shape
		    self.squares = [[self.mid,self.gridHeight],
				    [self.mid+1,self.gridHeight],
				    [self.mid,self.gridHeight-1],
				    [self.mid-1,self.gridHeight-1]]
		elif(self.type == 3): #Box
		    self.squares = [[self.mid, self.gridHeight],
				    [self.mid+1,self.gridHeight],
				    [self.mid-1,self.gridHeight],
				    [self.mid,self.gridHeight-1]] 
		elif(self.type == 4): #L shape left
		    self.squares = [[self.mid, self.gridHeight],
				    [self.mid, self.gridHeight-1],
				    [self.mid, self.gridHeight-2],
				    [self.mid-1, self.gridHeight-2]]
	 	elif(self.type == 5): #L shape right
		    self.squares = [[self.mid, self.gridHeight],
				    [self.mid, self.gridHeight-1],
				    [self.mid, self.gridHeight-2],
				    [self.mid+1, self.gridHeight-2]]
		elif(self.type == 6): #Z shape
		    self.squares = [[self.mid, self.gridHeight],
				    [self.mid-1, self.gridHeight],
				    [self.mid, self.gridHeight-1],
				    [self.mid+1, self.gridHeight-1]]
class Game:
	def __init__(self):
		self.tetroids = []
		self.gridHeight = 20
		self.gridWidth = 10
		self.currentTetroid = Tetroid(self)
		self.lines = 0
		self.check = False

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
	    self.tempSquares = []
	    self.origin = self.currentTetroid.squares[0]
	    print self.origin
	    for x in self.currentTetroid.squares:
		self.tempSquares.append([x[1] - self.origin[1] + self.origin[0], -x[0] + self.origin[0] + self.origin[1]])
	    self.tempSquares2 = self.currentTetroid.squares
	    self.currentTetroid.squares = self.tempSquares
	    for x in self.findLefts():
	        if( self.occupied(x[0],x[1]) or x[0] < 0):
		    self.currentTetroid.squares = self.tempSquares2
		    print "left"
		    return False
	    for x in self.findRights():
		if( self.occupied(x[0],x[1]) or x[0] >= self.gridWidth):
		    self.currentTetroid.squares = self.tempSquares2
		    print "right"
		    return False
	    for x in self.findMins():
		if( self.occupied(x[0],x[1]) or x[1] < 0 ):
		    self.currentTetroid.squares = self.tempSquares2
		    print x
		    print "min"
		    return False
 	    for x in self.findMaxs():
	        if( self.occupied(x[0],x[1]) or x[1] >= self.gridHeight ):
		    self.currentTetroid.squares = self.tempSquares2
		    print "max"
		    return False

	def occupied(self, x, y):
		for i in self.tetroids:
			for j in i.squares:
				if(j[0] == x and j[1] == y):
					return True
		return False

	def findLefts(self):	
		self.lefts = []
		for square in self.currentTetroid.squares:
		        self.lefts.append(square)
                        for x in self.lefts:
			    if(square[1] == x[1]): 
			        if( square[0] < x[0] ):
				    self.lefts.remove(x)
				elif( square[0] > x[0] ):
				    self.lefts.remove(square)
		return self.lefts

	def findRights(self):	
		self.rights = []
		for square in self.currentTetroid.squares:
		        self.rights.append(square)
                        for x in self.rights:
			    if(square[1] == x[1]): 
			        if( square[0] > x[0]):
				    self.rights.remove(x)
				elif( square[0] < x[0]):
				    self.rights.remove(square)
		return self.rights

	def findMins(self):	
		self.mins = []
		for square in self.currentTetroid.squares:
		        self.mins.append(square)
		        for x in self.mins:
			    if(square[0] == x[0]):
				if( square[1] < x[1]): 
			            self.mins.remove(x)
				elif(square[1] > x[1]):
				    self.mins.remove(square)
		return self.mins

	def findMaxs(self):
		self.maxs = []
		for square in self.currentTetroid.squares:
		        self.maxs.append(square)
		        for x in self.maxs:
			    if(square[0] == x[0]):
				if( square[1] > x[1]): 
			            self.maxs.remove(x)
				elif(square[1] < x[1]):
				    self.maxs.remove(square)
		return self.maxs

	def clearBelow(self):
		self.mins = self.findMins()	
		for coord in self.mins:
			if( coord[1] <= 0 ):
			    return False
			for x in self.tetroids:
				for y in x.squares:
					if( ( coord[0] == y[0] and coord[1]-1 == y[1] )  ):
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
		if(self.check):
			self.checkLines()
			self.tetroids.append(self.currentTetroid)
			self.currentTetroid = Tetroid(self)
			self.check = False

		if( not self.clearBelow() ):
		    self.check = True

		else:
			#Nothing below then move down
			for x in self.currentTetroid.squares:
				x[1] = x[1]-1

