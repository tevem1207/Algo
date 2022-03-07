import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())

computers = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

M = int(input())

for _ in range(M):
    com_a, com_b = map(int, input().split())
    computers[com_a].append(com_b)
    computers[com_b].append(com_a)

Q = deque(computers[1])

while Q:
    next_com = Q.popleft()
    if not visited[next_com]:
        visited[next_com] = 1
        Q.extend(computers[next_com])

print(sum(visited) - 1)
