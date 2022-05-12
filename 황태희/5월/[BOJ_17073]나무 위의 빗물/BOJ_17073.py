import sys 
sys.stdin = open('input1.txt') 


from collections import deque
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

q = deque([1])
visited = [0 for _ in range(1+N)]
visited[1] = 1
count = 0

while q:
    node = q.popleft()
    flag = 0
    for next_node in tree[node]:
        if not visited[next_node]:
            flag = 1
            q.append(next_node)
            visited[next_node] = 1
    if not flag:
        count += 1

print(W/count)


'''
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

count = 0

for node in tree[2:]:
    if len(node) == 1:
        count += 1

print(W/count)
'''
