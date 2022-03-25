import sys
sys.stdin = open('input.txt')


import sys
sys.setrecursionlimit(1000000)


def get_tree(node):
    global result

    for num in tree[node]:
        tree[num].remove(node)
        result[num] = node
        get_tree(num)


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0 for _ in range(N+1)]

get_tree(1)

for answer in result[2:]:
    print(answer)
