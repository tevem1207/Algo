import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline


def dfs(start):
    visited = [False for _ in range(n+1)]
    visited[start] = True
    stack = [[start, 0]]
    max_distance, max_node = 0, start
    while stack:
        now_node, now_distance = stack.pop()
        if now_distance > max_distance:
            max_distance, max_node = now_distance, now_node
        for next_node in tree[now_node]:
            if not visited[next_node]:
                stack.append([next_node, now_distance + tree[now_node][next_node]])
                visited[next_node] = True

    return max_distance, max_node


n = int(input())
tree = [{} for _ in range(n+1)]

target = set(range(1, n+1))

for _ in range(n-1):
    parent, child, distance = map(int, input().split())
    tree[parent][child] = distance
    tree[child][parent] = distance
    target -= {parent}

print(dfs(dfs(1)[1])[0])
