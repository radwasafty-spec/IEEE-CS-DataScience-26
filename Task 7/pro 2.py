import math

def b(n, k, p):
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

p = 0.12
n = 10

ans1 = sum(b(n, i, p) for i in range(0, 3))
ans2 = sum(b(n, i, p) for i in range(2, 11))

print(f"{ans1:.3f}")
print(f"{ans2:.3f}")