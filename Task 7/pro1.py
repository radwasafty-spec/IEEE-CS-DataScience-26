import math

def binomial_prob(n, k, p):
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

ratio_b, ratio_g = 1.09, 1
p = ratio_b / (ratio_b + ratio_g)
n = 6

result = sum(binomial_prob(n, i, p) for i in range(3, 7))

print(f"{result:.3f}")