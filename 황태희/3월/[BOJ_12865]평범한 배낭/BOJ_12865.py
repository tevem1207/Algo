import sys
sys.stdin = open('input.txt')


def solution(wt, vt, i):
    global result
    for j in range(i, len(arr)):
        if not visited[j]:
            w, v = arr[j]
            if wt+w > K:
                result.add(vt)
                break
            visited[j] = 1
            solution(wt+w, vt+v, j)
            visited[j] = 0


N, K = map(int, input().split())

arr = []

for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))
arr.sort()
visited = [0 for _ in range(N)]
result = set()
solution(0, 0, 0)
print(max(result))
