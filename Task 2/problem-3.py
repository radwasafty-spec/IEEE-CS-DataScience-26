n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

grades = sorted(list(set([x[1] for x in students])))
second_lowest = grades[1]

final_names = []
for s in students:
    if s[1] == second_lowest:
        final_names.append(s[0])

final_names.sort()

for name in final_names:
    print(name)