import random

from math import sqrt

def binomial(p):
	return int(random.random() < p)

def neutral_risk_prob(u, d, interest_rate):
	return ((1 + interest_rate - d) / (u - d))

def sample_variance(sample, mean):
	total = 0.0
	for element in sample:
		total += ((element - mean)**2)

	return sqrt(total / len(sample))