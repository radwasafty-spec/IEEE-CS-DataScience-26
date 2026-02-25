n = int(input("enter the number of players:"))
scores = list(map(int,input("enter every player score:").split()))
actualscores = set(scores)
sortedscores = sorted(list(actualscores))
print(sortedscores[-2])

