import math

def cumulative_phi(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

mean, std = 20, 2
val1 = 19.5
lower, upper = 20, 22

ans1 = cumulative_phi(val1, mean, std)
ans2 = cumulative_phi(upper, mean, std) - cumulative_phi(lower, mean, std)

print(f"{ans1:.3f}")
print(f"{ans2:.3f}")