from method_a import Montecarlo
from method_b import BinTree_method

print("== Método A ==")
print(Montecarlo(1, 1.1, 0.9, 0.025, 30, 10000000))

print("== Método B ==")
print(str(BinTree_method(30,1, 1.1, 0.9, 0.025)))