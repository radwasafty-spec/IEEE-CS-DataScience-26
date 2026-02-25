Num1 = float(input("enter first number:"))
Num2 = float(input("enter second number:"))
operator = input("enter operator( + , - , * , / ):")
if operator == "+":
    result = Num1 + Num2
elif operator == "-":
    result = Num1 - Num2
elif operator == "*":
    result = Num1 * Num2
elif operator == "/":
    result = Num1 / Num2
else:
    print("invalid operator")
print(f"the result is{result}")