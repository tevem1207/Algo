import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def go(n):
    visited[n] = True
    for m in graph[n][::-1]:
        if not visited[m]:
            go(m)
            
    
V, E = map(int, input().split())
visited = [False for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, g = map(int, input().split())
    graph[s].append(g)
    graph[g].append(s)

result = 0
for i in range(1, V+1):
    if not visited[i]:
        result += 1
        go(i)

print(result)
    
    