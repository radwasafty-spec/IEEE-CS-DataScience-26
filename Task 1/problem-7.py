s = input("enter a sentence")
words = s.split()
longestword = max(words, key=len)
print({longestword})