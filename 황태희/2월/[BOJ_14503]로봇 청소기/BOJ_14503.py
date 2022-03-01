import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
r, c, d = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
x, y = (c, r)
direction = (4 - d) % 4

while 1:
    matrix[y][x] = 2
    for _ in range(4):
        direction = (direction + 1) % 4
        dx, dy = delta[direction]
        if 0 <= x+dx < M and 0 <= y+dy < N:
            if not matrix[y+dy][x+dx]:
                x += dx
                y += dy
                break
    else:
        dx, dy = delta[direction]
        if 0 <= x - dx < M and 0 <= y - dy < N:
            if matrix[y-dy][x-dx] != 1:
                x -= dx
                y -= dy
            else:
                break
answer = 0

for i in range(N):
    answer += matrix[i].count(2)

print(answer)

