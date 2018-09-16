import random

def binomial(p):
	return int(random.random() < p)

def neutral_risk_prob(u, d, interest_rate):
	return ((1 + interest_rate - d) / (u - d))

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

	for i in range(n_sims):
		Vt = lookback_payoff(S0, u, d, interest_rate, n_steps)
		values += Vt

	mean = values / n_sims
	bonus = 1 / ((1 + interest_rate) ** n_steps) * mean

	return bonus

#print(Montecarlo(10, 1.1, 0.9, 0.02, 10, 100000))