import sys
sys.stdin = open('input2.txt')

N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

stu_grade = [[] for _ in range(7)]
for student in students:
    stu_grade[student[1]].append(student[0])

rooms = 0
for stu in stu_grade[1:]:
    boys = girls = 0
    for g in stu:
        if g:
            boys += 1
        else:
            girls += 1
    if boys:
        rooms = rooms + boys//K + 1 if boys % K else rooms + boys//K 
    if girls:
        rooms = rooms + girls//K + 1 if girls % K else rooms + girls//K 

print(rooms)
    