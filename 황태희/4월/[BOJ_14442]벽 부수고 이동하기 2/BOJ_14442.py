import sys 
sys.stdin = open('input2.txt')


from collections import deque


def solution(s):
    visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

    q = deque([(s[0], s[1], 0)])

    while q:
        x, y, wall_cnt = q.popleft()  # bfs 사용
        for dx, dy in delta:
            next_x, next_y = x+dx, y+dy
            if 0 <= next_x < M and 0 <= next_y < N:
                if matrix[next_y][next_x] == 3:
                    return visited[y][x][wall_cnt] + 2

                elif matrix[next_y][next_x] == 1:
                    if wall_cnt < K:
                        if not visited[next_y][next_x][wall_cnt+1]:
                            visited[next_y][next_x][wall_cnt+1] = visited[y][x][wall_cnt] + 1
                            q.append((next_x, next_y, wall_cnt+1))

                elif matrix[next_y][next_x] == 0:
                    if not visited[next_y][next_x][wall_cnt]:
                        visited[next_y][next_x][wall_cnt] = visited[y][x][wall_cnt] + 1
                        q.append((next_x, next_y, wall_cnt))
    return -1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, K = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
start = (0, 0)
matrix[0][0] = 2
matrix[N-1][M-1] = 3

if N == 1 and M == 1:
    print(1)
else:
    print(solution(start))
