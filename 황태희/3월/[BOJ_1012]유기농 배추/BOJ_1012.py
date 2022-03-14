import sys
sys.stdin = open('input.txt')


from collections import deque


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]


T = int(input())
for tc in range(1, T+1):
    cnt = 0
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    for y in range(N):
        for x in range(M):
            if matrix[y][x]:
                Q = deque([(x, y)])
                matrix[y][x] = 0
                while Q:
                    now_x, now_y = Q.popleft()
                    matrix[now_y][now_x] = 0
                    for dx, dy in delta:
                        next_x, next_y = now_x+dx, now_y+dy
                        if 0 <= next_x < M and 0 <= next_y < N and matrix[next_y][next_x]:
                            Q.append((next_x, next_y))
                            matrix[next_y][next_x] = 0
                cnt += 1

    print(cnt)
