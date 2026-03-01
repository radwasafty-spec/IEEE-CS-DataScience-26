def weightedMean(X, W):
    total_sum = sum(x * w for x, w in zip(X, W))
    sum_of_weights = sum(W)
    result = total_sum / sum_of_weights
    print(f"{result:.1f}")

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(vals, weights)