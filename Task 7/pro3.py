import math

def poisson(k, lamb):
    return (lamb**k * math.exp(-lamb)) / math.factorial(k)

lamb = 2.5
k = 5

result = poisson(k, lamb)

print(f"{result:.3f}")