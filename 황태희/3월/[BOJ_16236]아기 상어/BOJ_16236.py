import sys
sys.stdin = open('input.txt')

from collections import deque
import heapq


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]
fish_heap = []
target = set()
shark_size = 2
answer = 0
start = (-1, -1)

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 0:
            pass
        elif matrix[y][x] == 9:
            matrix[y][x] = 0
            baby_shark = (x, y)
        else:
            heapq.heappush(fish_heap, [matrix[y][x], x, y])

while fish_heap or target:
    eat = 0
    while fish_heap and shark_size > fish_heap[0][0]:
        fish = heapq.heappop(fish_heap)
        target.add((fish[1], fish[2]))

    can_eat = []

    if target:
        while target and start != baby_shark:
            start = baby_shark
            Q = deque([baby_shark])
            visited = set()
            visited.add(baby_shark)
            find = cnt = 0
            while Q:
                tmp = Q
                Q = deque()
                for x, y in tmp:
                    if (x, y) in target:
                        find = 1
                        can_eat.append((x, y))
                    else:
                        for dx, dy in delta:
                            next_x, next_y = x + dx, y + dy
                            if 0 <= next_x < N and 0 <= next_y < N and matrix[next_y][next_x] <= shark_size:
                                if (next_x, next_y) not in visited:
                                    Q.append([next_x, next_y])
                                    visited.add((next_x, next_y))
                if find:
                    can_eat.sort(key=lambda k: k[1])
                    target.remove(can_eat[0])
                    eat += 1
                    answer += cnt
                    baby_shark = (can_eat[0][0], can_eat[0][1])
                    can_eat = []
                    break
                else:
                    cnt += 1

            if eat == shark_size:
                shark_size += 1
                break

        if start == baby_shark:
            break
    else:
        break

print(answer)
