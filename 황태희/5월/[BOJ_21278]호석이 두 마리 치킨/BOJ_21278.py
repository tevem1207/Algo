import sys 
sys.stdin = open('input1.txt') 


from  collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = (float('inf'), (0, 0))
for i in range(1, N+1):
    for j in range(i+1, N+1):
        total = 0
        visited = [0 for _ in range(N+1)]
        for node in range(1, N+1):
            if node == i or node == j:
                pass
            else:
                q = deque([(node, 0)])
                while q:
                    now_node, cnt = q.popleft()
                    for next_node in graph[now_node]:
                        if next_node == i or next_node == j:
                            total += 2*(cnt+1)
                        elif not visited[next_node]:
                            q.append((next_node, cnt+1))
                            visited[next_node] = 1
                print(i, j, node, (cnt+1), total)
