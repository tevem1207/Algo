import heapq, sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if stack:
            print(-heapq.heappop(stack))
        else:
            print(0)
    else:
        heapq.heappush(stack, -x)
