import sys
sys.stdin = open('input.txt')


def find_fish(position):
    global baby_shark
    visited = set()
    now_p = [position]
    next_p = []
    target = []
    visited.add(position)
    for distance in range(1, N**2+1):
        for x, y in now_p:
            for dx, dy in delta:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < N and 0 <= next_y < N and matrix[next_y][next_x] <= shark_size:
                    if 0 < matrix[next_y][next_x] < shark_size:
                        target.append((next_x, next_y))
                    elif (next_x, next_y) not in visited:
                        next_p.append((next_x, next_y))
                        visited.add((next_x, next_y))
        if target:
            x, y = sorted(target, key=lambda k: (k[1], k[0]))[0]
            matrix[y][x] = 0
            baby_shark = (x, y)
            return distance
        now_p = next_p
        next_p = []
    return 0


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]
shark_size = 2
answer = 0
tmp = -1
eat = 0

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 9:
            matrix[y][x] = 0
            baby_shark = (x, y)
            break

while tmp != answer:
    tmp = answer
    answer += find_fish(baby_shark)
    if tmp != answer:
        eat += 1
        if eat == shark_size:
            eat = 0
            shark_size += 1

print(answer)
