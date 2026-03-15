import re

def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(is_valid_regex(s))