class Node:
	def __init__(self, number):
		self.number = number
		self.fathers = []
		self.children = []
		self.Vt = 0.0
		self.prob = 0.0
		self.minList = []