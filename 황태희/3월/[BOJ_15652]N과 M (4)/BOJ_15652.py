import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())

answers = [[] for _ in range(M)]
answers[0] = [[num] for num in range(1, N+1)]

for i in range(1, M):
    for arr in answers[i-1]:
        for num in range(arr[-1], N+1):
            answers[i].append(arr+[num])

for answer in answers[-1]:
    print(*answer)
