import sys
sys.stdin = open('input.txt')

from itertools import combinations
from collections import deque


N, M = map(int, input().split())
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
matrix = [list(map(int, input().split())) for _ in range(N)]
arr = []
viruses = []
wall_cnt = 0

for y in range(N):
    for x in range(M):
        if not matrix[y][x]:
            arr.append((x, y))
        else:
            wall_cnt += 1
            if matrix[y][x] == 2:
                viruses.append((x, y))

min_cnt = N * M
for walls in combinations(arr, 3):
    visited = set(walls)
    Q = deque(viruses)
    cnt = 0
    while Q:
        now_x, now_y = Q.popleft()
        for dx, dy in delta:
            next_x, next_y = now_x+dx, now_y+dy

            if 0 <= next_x < M and 0 <= next_y < N and matrix[next_y][next_x] == 0:
                if (next_x, next_y) not in visited:
                    Q.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    cnt += 1
        if cnt >= min_cnt:
            break

    if cnt <= min_cnt:
        min_cnt = cnt

print(N*M-min_cnt-wall_cnt-3)