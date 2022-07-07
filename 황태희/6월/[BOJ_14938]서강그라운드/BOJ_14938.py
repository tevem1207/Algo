import sys 
sys.stdin = open('input1.txt') 

import heapq


def dik(start):
    d = [float('inf') for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    d[start] = 0
    q = [[0, start]]
    while q:
        now_distance, now_node = heapq.heappop(q)
        visited[now_node] = 1
        for next_node, distance in graph[now_node].items():
            if not visited[next_node]:
                d[next_node] = min(d[next_node], now_distance + distance)
                heapq.heappush(q, [d[next_node], next_node])
    return d


n, m, r = map(int, input().split())
item_list = list(map(int, input().split()))
graph = [{} for _ in range(n+1)]
answer = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for field in range(1, n+1):
    result = dik(field)
    answer = max(answer, sum([item_list[i-1] for i in range(1, n+1) if result[i] <= m]))

print(answer)
