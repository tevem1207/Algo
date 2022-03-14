import sys
sys.stdin = open('input.txt')


delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]
N = int(input())

matrix = [list(input()) for _ in range(N)]
matrix_G = [['' for _ in range(N)] for _ in range(N)]
stack = []
cnt = cnt_G = 0

for i in range(N):
    for j in range(N):
        if matrix[j][i] == 'B':
            matrix_G[j][i] = 'B'
        else:
            matrix_G[j][i] = 'G'

for i in range(N):
    for j in range(N):
        if matrix[j][i]:
            color = matrix[j][i]
            matrix[j][i] = False
            stack.append((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in delta:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < N and 0 <= next_y < N and matrix[next_y][next_x] == color:
                        stack.append((next_x, next_y))
                        matrix[next_y][next_x] = False
            cnt += 1

        if matrix_G[j][i]:
            color_G = matrix_G[j][i]
            matrix_G[j][i] = False
            stack.append((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in delta:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < N and 0 <= next_y < N and matrix_G[next_y][next_x] == color_G:
                        stack.append((next_x, next_y))
                        matrix_G[next_y][next_x] = False
            cnt_G += 1

print(cnt, cnt_G)
