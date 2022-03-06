import sys

sys.stdin = open('input.txt')

from collections import deque


N = int(input())
visited = {N: 0}
Q = deque([N])

while True:
    X = Q.popleft()
    cnt = visited[X]
    if X == 1:
        print(cnt)
        break

    for next_X in [X/3, X/2, X-1]:
        if next_X == int(next_X) and next_X > 0 and next_X not in visited:
            Q.append(int(next_X))
            visited[int(next_X)] = cnt + 1
