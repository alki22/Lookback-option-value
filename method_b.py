import random

def neutral_risk_prob(u, d, interest_rate):
    return ((1 + interest_rate - d) / (u - d))

class Node:
    def __init__(self, number):
        self.number = number
        self.fathers = []
        self.children = []
        self.Vt = 0.0
        self.prob = 0.0
        self.minList = []

class BinomialTree:
    def __init__(self, n_periods):
        self.tree = []
        self.levels = n_periods        

        for i in range(n_periods):
            self.tree.append([])
        
        for level in range(n_periods):
            for k in range(level + 1):
                self.tree[level].append(Node(k))
        
        for level in range(n_periods - 1):
            for k in range(level + 1):
                current_node = self.tree[level][k].number
                self.tree[level][k].children = [k, k+1]
                self.tree[level + 1][k].fathers.append(current_node)
                self.tree[level + 1][k + 1].fathers.append(current_node)

    def lookback_option_values(self, s0, u, d, interest_rate):
        self.tree[0][0].Vt = s0
        for level in range(self.levels - 1):
                for k in range(level + 1):
                    self.tree[level + 1][k].Vt = self.tree[level][k].Vt * u
                    self.tree[level + 1][k + 1].Vt = self.tree[level][k].Vt * d
    
    def leafs_min_lists(self, u, d, interest_rate):
        p = neutral_risk_prob(u, d, interest_rate)
        
        self.tree[self.levels - 1][0].minList.append(self.tree[0][0].Vt)
        self.tree[self.levels - 1][0].prob = p ** (self.levels)
        
        self.tree[self.levels - 1][self.levels].minList.append(self.tree[0][0].Vt)
        self.tree[self.levels - 1][self.levels].prob = (1 - p) ** (self.levels)
        
        
B = BinomialTree(4)
print("Creado")
B.lookback_option_values(1,1.1,0.9,0.025)
print("Valor mas alto:")
print(B.tree[B.levels - 1][0].Vt)
print("Valor mas bajo:")
print(B.tree[B.levels - 1][B.levels - 1].Vt)
