class Node(object):		
	"""
		Node Object
	"""

	def __init__(self, localValue=0, globalValue=0, localLazy=0, globalLazy=0):
		self.localValue = localValue
		self.globalValue = globalValue
		self.localLazy = localLazy
		self.globalLazy = globalLazy


class SegmentTree2D(object):
	"""
		2D Segment Tree Class
	"""

	def __init__(self, n, m):
		"""
		Initializes the tree

		Arguments:
			n {int} -- number of rows in the matrix
			m {int} -- number of columns in the matrix
		"""


		self.n = n
		self.m = m
		self.tree = []				# Holds the nodes

		for i in range(4 * n):

			li = []

			for j in range(4 * m):
				li.append(Node())

			self.tree.append(li)

	def update(self, qxLo, qxHi, qyLo, qyHi, v):
		"""		
		Updates the tree by adding v to all elements within [qxLo:qxHi,qyLo:qyHi]
		
		Arguments:
			qxLo {int} -- start of x dimension
			qxHi {int} -- end of x dimension
			qyLo {int} -- start of y dimension
			qyHi {int} -- end of y dimension
			v {float/int} -- value to be added
		"""


		self.updateByX((1, 1), 1, self.n, qxLo, qxHi, qyLo, qyHi, v)	# update along x dimension

	def query(self, qxLo, qxHi, qyLo, qyHi):
		"""		
		Queries the sum of all elements within [qxLo:qxHi,qyLo:qyHi]
		
		Arguments:
			qxLo {int} -- start of x dimension
			qxHi {int} -- end of x dimension
			qyLo {int} -- start of y dimension
			qyHi {int} -- end of y dimension			
		"""

		return self.queryByX((1, 1), 1, self.n, qxLo, qxHi, qyLo, qyHi) # start querying along the x dimension

	def updateByX(self, nodeID, xLo, xHi, qxLo, qxHi, qyLo, qyHi, v):
		"""		
		Updates along x dimension
		
		Arguments:
			nodeID {tuple} -- (index along 1st layer tree, index along 2nd layer tree)
			xLo {int} -- start of x dimension of the region under the node
			xHi {int} -- end of x dimension of the region under the node
			qxLo {int} -- start of x dimension of update region
			qxHi {int} -- end of x dimension of update region
			qyLo {int} -- start of y dimension of update region
			qyHi {int} -- end of y dimension of update region	
			v {float/int} -- value to be added
		"""

		if (qxLo <= xLo and xHi <= qxHi):  # x is covered, intended update

			self.updateByY((nodeID[0], 1), xLo, xHi, 1, self.m, qxLo, qxHi, qyLo, qyHi, v, True)
			return

		elif (xLo > qxHi or xHi < qxLo):	# disjoint region

			return

		else:					# x is not fully covered, either a subregion or an overlapping region
								# dispersed update

			xMid = (xLo + xHi) // 2			# dividing the x region
			left = (nodeID[0] * 2, 1)
			right = (left[0] + 1, 1)

			self.updateByX(left, xLo, xMid, qxLo, qxHi, qyLo, qyHi, v)
			self.updateByX(right, xMid + 1, xHi, qxLo, qxHi, qyLo, qyHi, v)

			txLo = max(qxLo, xLo)		# trimming the x region
			txHi = min(qxHi, xHi)
			scaled_v =  v * ((1.0 * (txHi - txLo + 1)) / (xHi - xLo + 1)) 	# scaling

			self.updateByY((nodeID[0], 1), xLo, xHi, 1, self.m, txLo, txHi, qyLo, qyHi, scaled_v , False) # dispersed update

	def updateByY(self, nodeID, xLo, xHi, yLo, yHi, qxLo, qxHi, qyLo, qyHi, v, covered):
		"""		
		Updates along y dimension
		
		Arguments:
			nodeID {tuple} -- (index along 1st layer tree, index along 2nd layer tree)
			xLo {int} -- start of x dimension of the region under the node
			xHi {int} -- end of x dimension of the region under the node
			yLo {int} -- start of y dimension of the region under the node
			yHi {int} -- end of y dimension of the region under the node
			qxLo {int} -- start of x dimension of update region
			qxHi {int} -- end of x dimension of update region
			qyLo {int} -- start of y dimension of update region
			qyHi {int} -- end of y dimension of update region	
			v {float/int} -- value to be added, scaled appropriately
			covered {int} -- covered means that x region of the is contained within the update region
								1 : covered -> intended update
								0 : not covered -> dispersed update
		"""
		if (qyLo <= yLo and yHi <= qyHi):  # y is covered

			if (covered):		# x is covered, i.e. intended update

				self.tree[nodeID[0]][nodeID[1]].globalLazy += v
				self.tree[nodeID[0]][nodeID[1]].globalValue += v * (xHi - xLo + 1) * (yHi - yLo + 1)

			else:			# x is not covered, i.e. dispersed update

				self.tree[nodeID[0]][nodeID[1]].localLazy += v
				self.tree[nodeID[0]][nodeID[1]].localValue += v * (xHi - xLo + 1) * (yHi - yLo + 1)

			return


		elif (yHi < qyLo or qyHi < yLo):		# disjoint region

			return


		else:			# dividing the y region

			yMid = (yLo + yHi) // 2
			left = (nodeID[0], nodeID[1] * 2)
			right = (left[0], left[1] + 1)

			self.updateByY(left, xLo, xHi, yLo, yMid, qxLo, qxHi, qyLo, qyHi, v, covered)
			self.updateByY(right, xLo, xHi, yMid + 1, yHi, qxLo, qxHi, qyLo, qyHi, v, covered)

			self.tree[nodeID[0]][nodeID[1]].localValue = self.tree[left[0]][left[1]].localValue + self.tree[right[0]][right[1]].localValue + (self.tree[nodeID[0]][nodeID[1]].localLazy) * (xHi - xLo + 1) * (yHi - yLo + 1)
			self.tree[nodeID[0]][nodeID[1]].globalValue = self.tree[left[0]][left[1]].globalValue + self.tree[right[0]][right[1]].globalValue + (self.tree[nodeID[0]][nodeID[1]].globalLazy) * (xHi - xLo + 1) * (yHi - yLo + 1)

	def queryByX(self, nodeID, xLo, xHi, qxLo, qxHi, qyLo, qyHi):
		"""		
		Queries along x dimension
		
		Arguments:
			nodeID {tuple} -- (index along 1st layer tree, index along 2nd layer tree)
			xLo {int} -- start of x dimension of the region under the node
			xHi {int} -- end of x dimension of the region under the node
			qxLo {int} -- start of x dimension of update region
			qxHi {int} -- end of x dimension of update region
			qyLo {int} -- start of y dimension of update region
			qyHi {int} -- end of y dimension of update region				
		"""

		if (qxLo <= xLo and xHi <= qxHi):  # x is covered, complete query

			return self.queryByY((nodeID[0], 1), xLo, xHi, 1, self.m, qxLo, qxHi, qyLo, qyHi, 0)

		elif (xLo > qxHi or xHi < qxLo):		# disjoint region

			return 0.0

		else:				# x is not covered, partial query

			xMid = (xLo + xHi) // 2
			left = (nodeID[0] * 2, nodeID[1])
			right = (left[0] + 1, left[1])

			txLo = max(qxLo, xLo)		# trimming
			txHi = min(qxHi, xHi)
		
			
			return min(self.queryByY(nodeID, xLo, xHi, 1, self.m, txLo, txHi, qyLo, qyHi, 0), self.queryByX(left, xLo, xMid, qxLo, qxHi, qyLo, qyHi), self.queryByX(right, xMid + 1, xHi, qxLo, qxHi, qyLo, qyHi))
		

	def queryByY(self, nodeID, xLo, xHi, yLo, yHi, qxLo, qxHi, qyLo, qyHi, lazy):
		"""		
		Queries along y dimension
		
		Arguments:
			nodeID {tuple} -- (index along 1st layer tree, index along 2nd layer tree)
			xLo {int} -- start of x dimension of the region under the node
			xHi {int} -- end of x dimension of the region under the node
			yLo {int} -- start of y dimension of the region under the node
			yHi {int} -- end of y dimension of the region under the node
			qxLo {int} -- start of x dimension of update region
			qxHi {int} -- end of x dimension of update region
			qyLo {int} -- start of y dimension of update region
			qyHi {int} -- end of y dimension of update region	
			lazy {float/int} -- lazy value to be propagated			
		"""
		if (qyLo <= yLo and yHi <= qyHi):  # y is covered

			if (qxLo <= xLo and xHi <= qxHi):  # x is covered, complete query

				return min(self.tree[nodeID[0]][nodeID[1]].localValue, self.tree[nodeID[0]][nodeID[1]].globalValue + lazy * (xHi - xLo + 1) * (yHi - yLo + 1))

			elif (xLo > qxHi or xHi < qxLo):  # disjoint region (this will never happen)

				return 0.0

			else:				

				scaled_value = self.tree[nodeID[0]][nodeID[1]].globalValue * 1.0 * (qxHi - qxLo + 1) / (xHi - xLo + 1)

				return scaled_value + lazy * (qxHi - qxLo + 1) * (yHi - yLo + 1)


		elif (yLo > qyHi or yHi < qyLo):		# disjoint region

			return 0.0

		else:			
												# dividing along the y dimension
			yMid = (yLo + yHi) // 2
			left = (nodeID[0], nodeID[1] * 2)
			right = (left[0], left[1] + 1)

			if (qxLo <= xLo and xHi <= qxHi):  # x is covered, complete query

				return min(self.queryByY(left, xLo, xHi, yLo, yMid, qxLo, qxHi, qyLo, qyHi, lazy + self.tree[nodeID[0]][nodeID[1]].globalLazy + self.tree[nodeID[0]][nodeID[1]].localLazy), self.queryByY(right, xLo, xHi, yMid + 1, yHi, qxLo, qxHi, qyLo, qyHi, lazy + self.tree[nodeID[0]][nodeID[1]].globalLazy + self.tree[nodeID[0]][nodeID[1]].localLazy))
			

			elif (xLo > qxHi or xHi < qxLo):  # Disjoint region, This will never happen

				return 0.0

			else:		# x is not covered, partial query

				return min(self.queryByY(left, xLo, xHi, yLo, yMid, qxLo, qxHi, qyLo, qyHi, lazy + self.tree[nodeID[0]][nodeID[1]].globalLazy), self.queryByY(right, xLo, xHi, yMid + 1, yHi, qxLo, qxHi, qyLo, qyHi, lazy + self.tree[nodeID[0]][nodeID[1]].globalLazy))

r, c, l = [int(x) for x in input().split()]
segtree = SegmentTree2D(r, c)

for y in range(r):
    row = [int(a) for a in input().split()]
    for x in range(c):
        segtree.update(x, x, y, y, row[x])

print(segtree.query(0, 1, 0, 1))