n = int(input())
student_marks = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    student_marks[name] = marks

query_name = input()

g = student_marks[query_name]
ave = sum(g) / len(g)

print(f"{ave:.2f}")