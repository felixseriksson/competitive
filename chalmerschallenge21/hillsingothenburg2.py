# Python3 implementation to find the
# shortest path in a directed
# graph from source vertex to
# the destination vertex
class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second
infi = 1000000000

# Class of the node
class Node:

	# Adjacency list that shows the
	# vertexNumber of child vertex
	# and the weight of the edge 
	def __init__(self, vertexNumber):	 
		self.vertexNumber = vertexNumber
		self.children = []

	# Function to add the child for
	# the given node
	def Add_child(self, vNumber, length): 
		p = Pair(vNumber, length)
		self.children.append(p)
	
# Function to find the distance of
# the node from the given source
# vertex to the destination vertex
def dijkstraDist(g, s, path):
	
	# Stores distance of each
	# vertex from source vertex
	dist = [infi for i in range(len(g))]

	# bool array that shows
	# whether the vertex 'i'
	# is visited or not
	visited = [False for i in range(len(g))]
	
	for i in range(len(g)):	 
		path[i] = -1
	dist[s] = 0
	path[s] = -1
	current = s

	# Set of vertices that has
	# a parent (one or more)
	# marked as visited
	sett = set()	 
	while (True): 
		
		# Mark current as visited
		visited[current] = True
		for i in range(len(g[current].children)): 
			v = g[current].children[i].first		 
			if (visited[v]):
				continue

			# Inserting into the
			# visited vertex
			sett.add(v)
			alt = dist[current] + g[current].children[i].second

			# Condition to check the distance
			# is correct and update it
			# if it is minimum from the previous
			# computed distance
			if (alt < dist[v]):	 
				dist[v] = alt
				path[v] = current	 
		if current in sett:		 
			sett.remove(current)	 
		if (len(sett) == 0):
			break

		# The new current
		minDist = infi
		index = 0

		# Loop to update the distance
		# of the vertices of the graph
		for a in sett:	 
			if (dist[a] < minDist):		 
				minDist = dist[a]
				index = a		 
		current = index 
	return dist

# Function to print the path
# from the source vertex to
# the destination vertex
def printPath(path, i, s):
	if (i != s):
		# Condition to check if
		# there is no path between
		# the vertices
		if (path[i] == -1):	 
			print("Path not found!!")
			return	 
		printPath(path, path[i], s)
		print(path[i] + " ")
	

v = []
n = 4
s = 1
for i in range(1, n+1):
    a = Node(i)
    v.append(a)
    
v[0].Add_child(1, 1)
v[1].Add_child(0, 0)
v[0].Add_child(2, 0)
v[2].Add_child(0, 2)
v[1].Add_child(3, 0)
v[3].Add_child(1, 1)
v[2].Add_child(3, 2)
v[3].Add_child(2, 0) 
path = [0 for i in range(len(v))]
dist = dijkstraDist(v, s, path)
for i in range(len(dist)):
    if (dist[i] == infi):
        print("{0} and {1} are not " + "connected".format(i, s))
        continue	 
    print("Distance of {}th vertex from source vertex {} is: {}".format(i, s, dist[i]))