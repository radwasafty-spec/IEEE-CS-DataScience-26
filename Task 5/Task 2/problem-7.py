n = input("enter your text:").split()
count = 0
for word in n:
    if len(word) > 5:
        count += 1
    else:
        pass
print(count)    

    