num_str = input("enter a positive number:")
n = int(num_str)
sum_powers = 0
for digit in num_str :
    sum_powers += int(digit) **3
if n == sum_powers:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")