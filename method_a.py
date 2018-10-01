from math import sqrt
from prob import *

def lookback_payoff(S0, u, d, interest_rate, n_steps):
	p = neutral_risk_prob(u, d, interest_rate)
	St = S0
	min_value = S0

	for j in range(n_steps):
		x = binomial(p)
		
		if x == 1:
			St *= u
		else: 
			St *= d

		
		if St < min_value:
			min_value = St	

	return St - min_value

def Montecarlo(S0, u, d, interest_rate, n_steps, n_sims):
	values = 0.0
	sample = []

	for i in range(n_sims):
		Vt = lookback_payoff(S0, u, d, interest_rate, n_steps)
		sample.append(Vt)
		values += Vt

	mean = values / n_sims
	variance = sample_variance(sample, mean)
	error_rate = (variance / sqrt(n_sims))
	
	print("Error rate: " + str(error_rate))
	
	v0 = (1 / ((1 + interest_rate) ** n_steps)) * mean

	return v0