from BinomialTree import *

def BinTree_method(levels, s0, u, d, interest_rate):
	B = BinomialTree(levels, s0, u, d, interest_rate)
	
	return B.calculate_bonus(interest_rate)