from prob import *
from Node import *
from math import sqrt

class BinomialTree:
	def __init__(self, levels, s0, u, d, interest_rate):
		self.tree = []
		self.levels = levels		

		for period in range(levels):
			self.tree.append([])
		
		for level in range(levels):
			for k in range(level + 1):
				self.tree[level].append(Node(k))
		
		for level in range(levels - 1):
			for k in range(level + 1):
				current_node = self.tree[level][k].number
				self.tree[level][k].children = [k, k+1]
				self.tree[level + 1][k].fathers.append(current_node)
				self.tree[level + 1][k + 1].fathers.append(current_node)
		
		self.lookback_option_values(s0, u, d)
		self.leaves_min_lists(u, d, interest_rate)

	def lookback_option_values(self, s0, u, d):
		self.tree[0][0].Vt = s0
		for level in range(self.levels - 1):
				for k in range(level + 1):
					self.tree[level + 1][k].Vt = self.tree[level][k].Vt * u
					self.tree[level + 1][k + 1].Vt = self.tree[level][k].Vt * d
	
	def leaves_min_lists(self, u, d, interest_rate):
		p = neutral_risk_prob(u, d, interest_rate)
		q = 1.0 - p

		leaves = self.levels - 1 
		s0 = self.tree[0][0].Vt
		
		for level in range(leaves):
			for node in range(level + 1):
				current_node = self.tree[level][node]
				
				# for the tree's root, set min to s0 with probability of 1 
				if node == 0 and level == 0:
					self.tree[0][0].minList.append((s0, 1))

				for son in current_node.children:
					for minimum in current_node.minList:
						son_Vt = self.tree[level + 1][son].Vt
						son_index = current_node.children.index(son)
						p_or_q = (1 - son_index) * p + (0 + son_index) * q
						equal_min = [x for x in self.tree[level + 1][son].minList if x[0] == minimum[0]]
						
						if any(equal_min):
							equal_min_index = self.tree[level + 1][son].minList.index(equal_min[0])
							prev_min = self.tree[level + 1][son].minList.pop(equal_min_index)
							new_min = (prev_min[0], prev_min[1] + minimum[1] * p_or_q)
							self.tree[level + 1][son].minList.append(new_min)

						else:
							if minimum[0] <= son_Vt:
								self.tree[level + 1][son].minList.append(
									(minimum[0], minimum[1] * p_or_q))
							else:
								self.tree[level + 1][son].minList.append(
									(son_Vt, minimum[1] * p_or_q))

	def Vt_expected_value(self):
		leaves = self.levels - 1
		expected_value = 0.0

		# μ = Σ xi * pi
		for leaf in self.tree[leaves]:
			for minimum in leaf.minList:
				payoff = (leaf.Vt - minimum[0]) * minimum[1]
				expected_value += payoff
		return expected_value

	def calculate_bonus(self, interest_rate):
		v0 = (1 / ((1 + interest_rate) ** self.levels)) * self.Vt_expected_value()

		return v0