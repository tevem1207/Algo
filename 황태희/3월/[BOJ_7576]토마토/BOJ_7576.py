import sys
sys.stdin = open('input.txt')

from collections import deque


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cnt = 0
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
Q = deque()

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            Q.append((x, y))

while Q:
    tmp = []
    while Q:
        now_x, now_y = Q.popleft()

        for dx, dy in delta:
            next_x, next_y = now_x+dx, now_y+dy

            if 0 <= next_x < M and 0 <= next_y < N and matrix[next_y][next_x] == 0:
                tmp.append((next_x, next_y))
                matrix[next_y][next_x] = 1
    Q.extend(tmp)
    cnt += 1

for y in range(N):
    if 0 in matrix[y]:
        print(-1)
        break
else:
    print(cnt-1)
