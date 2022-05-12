import sys 
sys.stdin = open('input1.txt')


from collections import deque


N, L, R = map(int, input().split())
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
matrix = [list(map(int, input().split())) for _ in range(N)]

flag = 1
cnt = -1
while flag:
    cnt += 1
    flag = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tmp = [(j, i)]
                q = deque([(j, i)])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in delta:
                        if 0 <= x + dx < N and 0 <= y + dy < N:
                            if L <= abs(matrix[y][x] - matrix[y + dy][x + dx]) <= R:
                                if not visited[y+dy][x+dx]:
                                    q.append((x+dx, y+dy))
                                    visited[y+dy][x+dx] = 1
                                    tmp.append((x+dx, y+dy))
                if len(tmp) > 1:
                    total = 0
                    for x, y in tmp:
                        total += matrix[y][x]
                    for x, y in tmp:
                        matrix[y][x] = total//len(tmp)
                    flag = 1
print(cnt)
