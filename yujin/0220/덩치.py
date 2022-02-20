
N = int(input())

totals = [list(map(int, input().split())) for _ in range(N)]


person_list = []

for i in range(N):
    cnt = 0
    for name in range(N):
        if totals[i][0] < totals[name][0]:
            if totals[i][1] < totals[name][1]:
                cnt+=1
    person_list.append(cnt+1)

for i in person_list:
    print(i, end=' ')

'''
# 덩치 순위 메기기 위해서 본인보다 덩치 작은 사람 수 세기.
for i in range(N):
    cnt = 0
    for name in range(N):
        if totals[i][0] > totals[name][0]:
            if totals[i][1] > totals[name][1]:
                cnt+=1
    person_list.append(cnt)

# rank 메기기 위해서 자신보다 많은 사람 수 가진 사람 만나면 rank +1씩.
for i in range(N):
    rank = 1
    for num in range(N):
        if person_list[i] < person_list[num]:
            rank+=1
    rank_list.append(rank)

for i in rank_list:
    print(i, end=' ')
'''