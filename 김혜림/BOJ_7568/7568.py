# 덩치
import sys
sys.stdin = open('input.txt')

N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

def bigger_num(idx):
    cnt = 0
    for j in range(N):
        if people[j][0] > people[idx][0] and people[j][1] > people[idx][1]:
            cnt += 1
    return cnt

cnt_list = []

for i in range(N):
    cnt_list.append(bigger_num(i))

answer_list = []
for i in range(N):
    cnt2 = 1
    for j in range(N):
        if cnt_list[i] > cnt_list[j]:
            cnt2 += 1
    answer_list.append(cnt2)
print(' '.join(map(str, answer_list)))