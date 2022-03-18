import sys
sys.stdin = open('input.txt')


from collections import deque


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(end):
    q = deque([(0, 0, 0)])
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while q:
        now_x, now_y, is_break = q.popleft()
        if (now_x, now_y) == end:
            return visited[now_y][now_x][is_break]
        for dx, dy in delta:
            next_x, next_y = now_x+dx, now_y+dy
            if 0 <= next_x < M and 0 <= next_y < N:
                if not visited[next_y][next_x][is_break] and not visited[next_y][next_x][is_break*0]:
                    if matrix[next_y][next_x]:
                        # 벽 부수기
                        if not is_break:
                            visited[next_y][next_x][is_break+1] = visited[now_y][now_x][is_break] + 1
                            q.append((next_x, next_y, is_break+1))
                    else:
                        # 그냥 통과
                        visited[next_y][next_x][is_break] = visited[now_y][now_x][is_break] + 1
                        q.append((next_x, next_y, is_break))
    return -1


N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]


print(bfs((M-1, N-1)))
