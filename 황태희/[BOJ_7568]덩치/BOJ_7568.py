import sys
sys.stdin = open('input.txt')


N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

answer_list = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            cnt += 1
    answer_list.append(cnt)

print(' '.join(map(str, answer_list)))