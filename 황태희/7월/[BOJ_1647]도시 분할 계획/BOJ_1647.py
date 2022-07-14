import sys 
sys.stdin = open('input1.txt') 

import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0 for _ in range(N+1)]
for i in range(1, N+1):
    parent[i] = i

edges = []
total_cost = []

for i in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(M):
    cost, a, b = edges[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost.append(cost)

print(sum(sorted(total_cost)[:-1]))
