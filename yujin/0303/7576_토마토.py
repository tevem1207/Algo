import sys
from collections import deque
sys.stdin = open("input.txt")

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1,-1, 0, 0], [0, 0, 1, -1]
get_point = []
get_point = deque(get_point)

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            get_point.append([i,j])


def get_bfs(y,x):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < M and 0 <= ny < N and tomato[ny][nx] == 0:
            get_point.append([ny, nx])
            tomato[ny][nx] = tomato[y][x] + 1
        elif 0 <= nx < M and 0 <= ny < N and tomato[ny][nx] == -1:
            continue
        else:
            continue

result = 0
max = 0

while get_point:
    y, x = get_point.popleft()
    get_bfs(y,x)

for i in range(N):
    for j in range(M):
        if tomato[i][j] > max:
            max = tomato[i][j]
result = max-1

for i in range(N):
    if tomato[i].count(0) > 0:
        result = -1
        break;


print(f'{result}')