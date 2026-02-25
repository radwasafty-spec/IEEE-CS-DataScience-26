n = int(input("enter a number:"))
for i in range (1, 11):
    result = n * i
    if result % 4 == 0:
        continue
    print(f"{result}")