from math import sqrt
from prob import *


def Montecarlo(S0, u, d, interest_rate, n_steps, error_rate):
    mean = sample_mean(S0, u, d, interest_rate, n_steps, error_rate)
    v0 = (1 / ((1 + interest_rate) ** n_steps)) * mean

    return v0

print(Montecarlo(1, 1.1, 0.9, 0.025, 30, 0.001))
