def solution(y):
    global result
    if y < N:
        for x in range(N):
            # add
            for i in range(y):
                if visited[i] == x or visited[i] - x == i - y or visited[i] - x == y - i:
                    break
            else:
                visited[y] = x
                solution(y + 1)
                visited[y] = -1
    else:
        result += 1


N = int(input())
visited = [-1 for _ in range(N)]
result = 0

solution(0)

print(result)
