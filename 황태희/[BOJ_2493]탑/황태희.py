N = int(input())

towers = list(zip(map(int, input().split()), range(N)))
stack = [towers.pop()]
answer = [0 for _ in range(N)]

while towers:
    while stack:
        if towers[-1][0] > stack[-1][0]:
            tower = stack.pop()
            answer[tower[1]] = towers[-1][1] + 1
        else:
            break
    stack.append(towers.pop())

print(*answer)
