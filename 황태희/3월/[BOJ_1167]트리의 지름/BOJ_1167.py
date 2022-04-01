import sys
sys.stdin = open('input.txt')


import heapq


def get_distance(start):
    d = [float('inf') for _ in range(V+1)]
    d[start] = 0
    q = [[0, start]]

    while q:
        now_distance, now_node = heapq.heappop(q)
        for next_node in tree[now_node]:
            next_distance = now_distance + tree[now_node][next_node]
            if d[next_node] > next_distance:
                d[next_node] = next_distance
                heapq.heappush(q, [next_distance, next_node])

    return now_node, now_distance


V = int(input())
tree = [{} for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range((len(arr)-2)//2):
        tree[arr[0]][arr[2 * i + 1]] = arr[2 * i + 2]

print(get_distance(get_distance(1)[0])[1])