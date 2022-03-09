import sys
sys.stdin = open('input.txt')

from collections import deque


N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = 0

for i in range(1, N+1):
    if not visited[i]:
        Q = deque(arr[i])
        answer += 1

    while Q:
        tmp = Q.popleft()
        if not visited[tmp]:
            visited[tmp] = 1
            Q.extend(arr[tmp])

print(answer)
