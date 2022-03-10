import sys
sys.stdin = open('input.txt')


def go(c):
    visited[c] = True
    for new_c in graph[c][::-1]:
        if not visited[new_c]:
            go(new_c)
            
            
computer = int(input())
E = int(input())  # 직접 연결돼 있는 컴퓨터 수 Edge

graph = [[] for _ in range(computer+1)]
for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False for _ in range(computer+1)]
go(1)

result = 0
for idx in range(computer+1):
    if idx != 1 and visited[idx]:
        result += 1

print(result)