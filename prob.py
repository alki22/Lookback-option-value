import random

from math import sqrt


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


def sample_mean(s0, u, d, interest_rate, n_steps, error_rate):
	mean = lookback_payoff(s0, u, d, interest_rate, n_steps)
	Scuad = 0
	n = 1

	while(n <= 100000000):
		n += 1
		Vt = lookback_payoff(s0, u, d, interest_rate, n_steps)
		former_mean = mean
		mean = mean + (Vt - mean) / n
		Scuad = Scuad * (1 - 1 / (n - 1)) + n * ((mean - former_mean) ** 2)
		if (sqrt(Scuad / n) < error_rate):
			print(n)
			break

	return mean