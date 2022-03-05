import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(s, e):
    q = deque([s])
    visited = {s: 0}
    while q:
        p = q.popleft()
        cnt = visited[p]
        if p == e:
            return cnt
        for next_p in [p - 1, p * 2, p + 1]:
            if (next_p not in visited) and 0 <= next_p <= 100000:
                q.append(next_p)
                visited[next_p] = cnt + 1


N, K = map(int, input().split())
print(bfs(N, K))
