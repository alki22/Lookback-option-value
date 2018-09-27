import random

class Node:
	def __init__(self, number, Vt=0.0, binTree):
		self.number = number
		self.fathers = []
		self.children = []
		self.Vt = Vt
		self.minList = []
		
	def calculateVt(self, binTree, u, d):
		index = binTree.tree[self.fathers[0]].children.index(self.number)
		self.Vt = (1 - index) * u + (0 + index) * d

class BinomialTree:
	def __init__(self, n_periods, s0):
		self.tree = []
		n_leafs = int((n_periods + 1) * (n_periods + 2) / 2)
		
		for i in range(n_leafs):
			self.tree.append(Node(number=i, binTree=self.tree))
			
		
