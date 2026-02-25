string = input("enter a string:").lower()
vowels = [ "a" , "e" , "i" , "o" , "u"  ]
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"the number of vowels:{count}")        